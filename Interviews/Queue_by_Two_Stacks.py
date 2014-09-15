"""
Implement a Queue by using two stacks. Support O(1) push, pop, top
"""

class Queue():
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, num):
        self.inbox.append(num)

    def pop(self):
        if not self.outbox:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

    def top(self):
        if not self.outbox:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]