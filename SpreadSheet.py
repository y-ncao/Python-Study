#!/usr/bin/env python

class Cell():
    def __init__(self, row, col, expression):
        self.row = row
        self.col = col
        self.expression = expression
        self.dependencies = []
        self.value = value

    def get_expression():
        return self.expression

    def set_expression(expression):
        self.expression = expression

    def get_value():
        return self.value

    def get_dependencies():
        return self.dependencies

    def add_dependency(cell):
        self.dependencies.append(cell)

    def set_indegree(d):
        self.indegree = d

    def decrement_indegree():
        self.indegree -= 1
        return self.indegree

    def solve():
        stack = []
        elements = self.expression.split()
        for el in elements:
            if el.isdigit():
                stack.append(float(el))
            elif el[0].isalpa() and el[0].istitle()

class SpreadSheet():
    def __init__(self):
        size_info = raw_input("Please enter the size of SpreadSheet in format: 'col row'\n")
        self.len_col = int(size_info.split()[1])
        self.len_row = int(size_info.split()[0])

        if self.len_row > 26:
            raise ValueError('Row should be no bigger than 26')

        self.sheet = [ [None for j in range(self.len_col)] for i in range(self.len_row) ]
        for i in range(self.len_row):
            for j in range(self.len_col):
                  cell_input = raw_input("Please enter the row %s, col %d\n" % (chr(65+i), j+1))
                  self.sheet[i][j] = Cell(i, j, cell_input)

        print self.sheet

a = SpreadSheet()
