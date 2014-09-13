#!/usr/bin/env python

class CyclicDependencyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Cell():
    def __init__(self, expression, sheet):
        self.expression = expression
        self.dependencies = []
        self.value = None
        self.sheet = sheet

    def get_expression(self):
        return self.expression

    def get_value(self):
        return self.value

    def get_dependencies(self):
        return self.dependencies

    def add_dependency(self, cell):
        self.dependencies.append(cell)

    def set_indegree(self, indegree):
        self.indegree = indegree

    def get_indegree(self):
        return self.indegree

    def decrement_indegree(self):
        self.indegree -= 1
        return self.indegree == 0

    def get_reference(self):
        refs = []
        elements = self.expression.split()
        for el in elements:
            if el[0].isalpha() and el[0].istitle():
                refs.append(el)
        self.set_indegree(len(refs))
        return refs

    def _calculate(self, num_1, num_2, operator):
        oper_dict = { '+': lambda x, y: x+y,
                      '-': lambda x, y: x-y,
                      '*': lambda x, y: x*y,
                      '/': lambda x, y: x/y,
                      '++': lambda x, y: x+1,
                      '--': lambda x, y: x-1,
                      }
        return oper_dict[operator](num_1, num_2)

    def solve_cell(self):
        stack = []
        elements = self.expression.split()
        for el in elements:
            # el is number (Supporting negative numbers)
            if el.isdigit() or ( len(el) >= 2 and el[0] == '-' and el[1:].isdigit() ):
                stack.append(float(el))

            # el is cell reference
            elif el[0].isalpha() and el[0].istitle():
                stack.append(self.sheet.get_cell_from_ref(el).get_value())

            # el is '++' or '--' (Supporting '++' '--')
            elif el in ['++', '--']:
                last = stack.pop()
                result = self._calculate(last, None, el)
                stack.append(result)

            # el is operator
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()
                result = self._calculate(num_1, num_2, el.strip())
                stack.append(result)

        self.value = stack.pop()


class SpreadSheet():
    def __init__(self, row=None, col=None, sheet_array=None):
        if not row and not col:
            size_info = raw_input("Please enter the size of SpreadSheet in format: 'col row'\n")
            self.len_row = int(size_info.split()[1])
            self.len_col = int(size_info.split()[0])
        else:
            self.len_row = row
            self.len_col = col

        if self.len_row > 26:
            raise ValueError('Row should be no bigger than 26')

        self.sheet = [ [None for j in range(self.len_col)] for i in range(self.len_row) ]
        if not sheet_array:
            for i in range(self.len_row):
                for j in range(self.len_col):
                      cell_input = raw_input("Please enter the row %s, col %d\n" % (chr(65+i), j+1))
                      self.sheet[i][j] = Cell(cell_input, self)
        else:
            for i in range(row):
                for j in range(col):
                    self.sheet[i][j] = Cell(sheet_array[i][j], self)

    def get_cell_from_ref(self, ref):
        row = ord(ref[0]) - ord('A')
        col = int(ref[1]) - 1
        return self.sheet[row][col]

    def gen_top_graph(self):
        self.top_graph = TopGraph(self.len_col * self.len_row)
        for i in range(self.len_row):
            for j in range(self.len_col):
                cell = self.sheet[i][j]
                refs = cell.get_reference()
                if len(refs) == 0:
                    self.top_graph.enqueue(cell)
                else:
                    for ref in refs:
                        cd = self.get_cell_from_ref(ref)
                        cd.add_dependency(cell)
        return self.top_graph

    def output(self):
        self.top_graph = self.gen_top_graph()
        self.top_graph.solve()

        output_result = [ [None for j in range(self.len_col)] for i in range(self.len_row) ]
        for i in range(self.len_row):
            for j in range(self.len_col):
                output_result[i][j] = '%.5f' % self.sheet[i][j].get_value()

        return output_result

class TopGraph():
    def __init__(self, size):
        self.checked_cell = 0
        self.size = size
        self.queue = []

    def enqueue(self, cell):
        self.queue.insert(0, cell)

    def dequeue(self):
        return self.queue.pop()

    def solve(self):
        while self.queue:
            cell = self.dequeue()
            self.checked_cell += 1
            cell.solve_cell()
            for depen in cell.get_dependencies():
                if depen.decrement_indegree():
                    self.enqueue(depen)

        if self.checked_cell < self.size:
            raise CyclicDependencyError('Cannot solve due to cyclic dependency!')

    # Solving steps:
    # 1. Prepare for sheet content
    # 2. generate topological graph
    # 3. solve topological graph
    # 4. print output

if __name__ == '__main__':
    test_sheet_1 = SpreadSheet(row=2, col=3,
                             sheet_array=[['A2', '4 5 *', 'A1'],
                                          ['A1 B2 / 2 +', '3', '39 B1 B2 * /']])

    print test_sheet_1.output()

    test_sheet_2 = SpreadSheet(row=2, col=3,
                             sheet_array=[['A2', '-4 5 *', 'A1 ++'],
                                          ['A1 B2 / 2 +', '3 --', '39 B1 B2 * /']])

    print test_sheet_2.output()

    test_sheet_3 = SpreadSheet()
    print test_sheet_3.output()
