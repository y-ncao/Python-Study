"""
#####From NC Class 7 Data Structures, slides 8
[Solution](http://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/)
"""

class MinStack():
    def __init__(self, size):
        self.data_stack = []
        self.min_stack = []
        self.size = size

    def is_full(self):
        return len(self.data_stack) == self.size

    def is_empty(self):
        return not self.data_stack

    def push(self, data):
        if self.is_full():
            return False
        self.data_stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        if self.is_empty():
            return False
        data = self.data_stack.pop()
        if data == self.min_stack[-1]:
            self.min_stack.pop()
        return data

    def get_min(self):
        return self.min_stack[-1]
