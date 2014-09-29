#!/usr/bin/env python

# Author: Yan Cao
# Date:   9/13/2014

class Cell():
    def __init__(self, expression, sheet):
        self.expression = expression
        self.value = None
        self.dependencies = []
        self.sheet = sheet

    def get_expression(self):
        return self.expression

    def get_value(self):
        return self.value

    def set_indegree(self, indegree):
        self.indegree = indegree

    def get_indegree(self):
        return self.indegree

    def get_dependencies(self):
        return self.dependencies

    def add_dependency(self, cell):
        self.dependencies.append(cell)

    def decrement_indegree(self):
        self.indegree -= 1
        return self.indegree

    def get_reference(self):
        refs = []
        elements = self.expression.split()
        for el in elements:
            if el[0].isalpha() and el[0].istitle():
                refs.append(el)
        self.set_indegree(len(refs))
        return refs

    def _calculate(self, num_1, num_2, operator):
        oper_dict = { '+' : lambda x, y: x+y,
                      '-' : lambda x, y: x-y,
                      '*' : lambda x, y: x*y,
                      '/' : lambda x, y: x/y,
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
                if len(stack) < 2:
                    raise Exception('Cell expression error! Expression is %s' % self.expression)
                num_2 = stack.pop()
                num_1 = stack.pop()
                result = self._calculate(num_1, num_2, el.strip())
                stack.append(result)

        if len(stack) > 1:
            raise Exception('Cell expression error! Expression is %s' % self.expression)

        self.value = stack.pop()


class SpreadSheet():
    def __init__(self, row=None, col=None, sheet_array=None, input_file=None):
        if input_file:
            with open(input_file, 'r') as f:
                lines = f.readlines()
                f.close()
                self.len_row = int(lines[0].split()[1])
                self.len_col = int(lines[0].split()[0])
        else:
            self.len_row = row
            self.len_col = col

        if self.len_row > 26:
            raise ValueError('Row should be no bigger than 26')

        self.sheet = [ [None for j in range(self.len_col)] for i in range(self.len_row) ]

        if input_file:
            if len(lines) -1 != self.len_row * self.len_col:
                raise Exception('Input file length error! Should be %d, but has %d lines' % \
                                (self.len_row * self.len_col, len(lines)))
            i = 1
            while i < len(lines):
                self.sheet[(i-1) / self.len_col][(i-1) % self.len_col] = Cell(lines[i], self)
                i += 1
        else:
            for i in range(row):
                for j in range(col):
                    self.sheet[i][j] = Cell(sheet_array[i][j], self)

    def get_cell_from_ref(self, ref):
        row = ord(ref[0]) - ord('A')
        col = int(ref[1]) - 1
        return self.sheet[row][col]

    def _gen_graph(self):
        self.graph = Graph(self.len_col * self.len_row)
        for i in range(self.len_row):
            for j in range(self.len_col):
                cell = self.sheet[i][j]
                refs = cell.get_reference()
                if not refs:
                    self.graph.enqueue(cell)
                else:
                    for ref in refs:
                        ref_cell = self.get_cell_from_ref(ref)
                        ref_cell.add_dependency(cell)
        return self.graph

    def output(self):
        self.graph = self._gen_graph()
        self.graph.solve()

        output_result = [ [None for j in range(self.len_col)] for i in range(self.len_row) ]
        for i in range(self.len_row):
            for j in range(self.len_col):
                output_result[i][j] = '%.5f' % self.sheet[i][j].get_value()

        return output_result


class Graph():
    def __init__(self, size):
        self.checked_cells = 0
        self.size = size
        self.queue = []

    def enqueue(self, cell):
        self.queue.insert(0, cell)

    def dequeue(self):
        return self.queue.pop()

    def solve(self):
        while self.queue:
            cell = self.dequeue()
            self.checked_cells += 1
            cell.solve_cell()
            for dp_cell in cell.get_dependencies():
                if dp_cell.decrement_indegree() == 0:
                    self.enqueue(dp_cell)

        if self.checked_cells < self.size:
            raise Exception('Cannot solve due to cyclic dependency!')

    # Solving steps:
    # 1. Prepare for sheet content
    # 2. generate graph
    #    i. set up dependencies
    #    ii. enqueue all zero reference cells
    # 3. use topological sort to solve graph
    #    i. solve the cell with zero reference
    #    ii. enqueue dependency cell if cell has indegree == 1
    #    iii. repeat i, ii until nothing left in queue.
    #         if not all cells are solved, we have cyclic dependency
    # 4. print output

    # Some thoughts about scale:
    # 1. To scale, basically should use some MapReduce to split spreadsheet to several small spreadsheets
    # 2. Map: try to solve all the cells within each small spreadsheet, however
    #    i.  if the small spreadsheet is solvable(no cell referencing cells outside this sheet),
    #        mark it as complete.
    #    ii. if there's a cell referencing cells in other small spreadsheet,
    #        mark it as incomplete and need to keep it for the reduce function
    # 3. Reduce: combine each small spreadsheet, if any spreadsheet is not solved yet, solve it.
    #            if still have unsolvable cells, we are having cyclic dependency.
    # 4. The tricky part would be, how small do we want to split the spreadsheet.
    #    Key factors:
    #    i.  size of data (larger amount of data, more splits)
    #    ii. how many cells are referencing each other(less referencing can do more splits)
    # But basically I just want to say, this design is scalable.

if __name__ == '__main__':
    test_sheet_1 = SpreadSheet(row=2, col=3,
                             sheet_array=[['A2', '4 5 *', 'A1'],
                                          ['A1 B2 / 2 +', '3', '39 B1 B2 * /']])
    print '\nTest case provided by Quantcast'
    print test_sheet_1.output()

    test_sheet_2 = SpreadSheet(row=2, col=3,
                             sheet_array=[['A2', '-4 5 *', 'A1 ++'],
                                          ['A1 B2 / 2 +', '3 --', '39 B1 B2 * /']])

    print '\n With negative numbers and ++ --'
    print test_sheet_2.output()

    print '\nFrom stdin'
    test_sheet_3 = SpreadSheet(input_file='test_case.txt')
    print test_sheet_3.output()


    test_sheet_4 = SpreadSheet(row=2, col=3,
                             sheet_array=[['A3', '-4 5 *', 'A1 ++'],
                                          ['A1 B2 / 2 +', '3 --', '39 B1 B2 * /']])
    print '\nWith cyclic dependency'
    print test_sheet_4.output()
