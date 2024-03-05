from collections import deque

class stack:
    def __init__(self):
        self.stack = deque()
        self.stack_size = 5
    def push(self, data):
        if len(self.stack) < self.stack_size:
            self.stack.append(data)
        else:
            print('Overflow stack is full !')
    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            print('Underflow the stack is empty')
    def display(self):
        if self.stack:
            return self.stack
    def min_val(self):
        if self.stack:
            return min(self.stack)
        return 'its empty'
    
stack = stack()
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)

# overflow
stack.push(1)
print(stack.display())
stack.pop()
print(stack.display())
stack.push(88)
print('Pushed at End !')
print(stack.display())
stack.pop()
print('Popped at end')
print(stack.display())
print(stack.min_val())

