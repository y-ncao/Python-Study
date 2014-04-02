#!/usr/bin/env python

# In python, we use list function append() as push
# pop() as pop
# For Queue, use from collections import deque as queue
# Use append() as push, use popleft() as pop

class my_queue:
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

class new_stack:
    def __init__(self):
        self.stack = []
        self.min = None
        self.min_list = []

    def pop(self):
        self.min_list.pop()
        return self.stack.pop()
        
    def push(self, data):
        if data < self.min_list[len(min_list)-1]:
            self.min_list.append(data)
        else:
            self.min_list.append(self.min_list[len(min_list)-1])
        self.stack.append(data)

    def get_min(self):
        return self.min_list.pop()

def sort_stack1(stack):
    temp_stack = [stack.pop(),]
    temp_var = None
    while len(stack) > 0:
        temp_var = stack.pop()
        while len(temp_stack)>0 and temp_stack[len(temp_stack)-1] > temp_var:
            stack.append(temp_stack.pop())
        temp_stack.append(temp_var)

    return temp_stack

def sort_stack(stack):
    temp = [stack.pop(),]
    while len(stack) > 0:
        print '*'*10
        print 'in stack',stack
        print 'in temp',temp
        # check if should put equal here
        if stack[len(stack)-1] >= temp[len(temp)-1]:
            print 'pushing to temp'
            temp.append(stack.pop())
        else:
            var = stack.pop()
            while len(temp) > 0:
                print 'VAR',var
                if var is None or var < temp[len(temp)-1]:
                    print 'temp peek', temp[len(temp)-1]
                    stack.append(temp.pop())
                    print 'temp_stack', temp
                else:
                    print 'appending var'
                    stack.append(var)
                    var = None
            # VERRRRRRRRRRY IMPORTANT, don't forget to push the last var
            if var is not None:
                temp = [var,]
            else:
                temp = [stack.pop(),]
    return temp

class Animal:
    def __init__(self, name):
        self.name  = name

    def set_order(self, order):
        self.order = order

    def get_order(self, order):
        return self.order

    def is_older_than(Animal):
        if self.order < Animal.get_order():
            return True
        else:
            return False
    
class Cat(Animal):
    def __init__(self, name):
        self.super()

class Dog(Animal):
    def __init__(self, name)

from collection import deque

class AnimalQueue:
    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()
        self.order = 0

    def add_animal(self, animal):
        if isinstance(animal, Cat):
            cat_queue.append(animal)
        else:
            dog_queue.append(animal)
        animal.set_order(order)
        self.order += 1

    def deq_dog(self):
        if len(self.dog_queue) == 0:
            return 'No dog left'
        return self.dog_queue.popleft()

    def deq_cat(self):
        if len(self.cat_queue) == 0:
            return 'No cat left'
        return self.cat_queue.popleft()

    def deq_any(self):
        if len(self.cat_queue) == 0 and len(self.dog_queue) ==0:
            return 'No Animal Left!'
        elif len(self.cat_queue) == 0:
            self.deq_dog()
        elif len(self.dog_queue) == 0:
            self.deq_cat()
        # Great, you have the chance to get either a cat or dog
        else:
            if cat_queue[0].is_older_than(dog_queue[0]):
                self.deq_cat()
            else:
                self.deq_dog()

# Missing 3.1 3.3 3.4
if __name__ == '__main__':
    stack = [8,4,7,9,2,1,6,5,10]
    new_stack = sort_stack(stack)
    print new_stack
    
