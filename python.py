from collections import deque

class stack:
    def __init__(self):
        self.stack = deque()
        self.stack_size = 5
    def push(self, data):
        if len(self.stacck) < self.stack_size:
            self.stack.append(data)
        else:
            print('Stack is Overflow !!')
    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            print('Stack is underflow !!')
    
    def display(self):
        if self.stack:
            return self.stack
    def min_val(self):
        if self.stack:
            return min(self.stack)
        return 'its empty'
