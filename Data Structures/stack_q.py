#!/usr/bin/env python

# In python, we use list function append() as push
# pop() as pop
# For Queue, use from collections import deque as queue
# Use append() as push, use popleft() as pop

class my_queue():
    def __init__(self):
        self.stack_a = []
        self.stack_b = []
        self.storing_a = True

    def push(self, data):
        if storing_a:
            self.stack_a.append(data)
        else:
            self.stack_b.append(data)

    def pop(self):
        # Data is in A, so first push data to B and pop the last one in queue
        if storing_a:
            while len(a)>0:
                b.append(a.pop())
            storing_a = False
            return b.pop()
        else:
            while len(b)>0:
                a.append(b.pop())
            storing_a = True
            return a.pop()

def sort_stack(stack):
    temp_stack = [stack.pop(),]
    temp_var = None
    while len(stack) > 0:
        temp_var = stack.pop()
        while len(temp_stack)>0 and temp_stack[len(temp_stack)-1] > temp_var:
            stack.append(temp_stack.pop())
        temp_stack.append(temp_var)

    return temp_stack

if __name__ == '__main__':
    stack = [8,4,7,9,2,1,6,5,10]
    new_stack = sort_stack(stack)
    print new_stack
