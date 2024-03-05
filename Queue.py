#conceptual code
#Queue implementation in python 
from collections import deque
class Queue_Implementation: 
    def __init__(self):
        self.queue=deque()
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.queue:
            self.queue.popleft()
        else:
            print("queue is empty")
    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return 'Its empty'
    def display(self):
        if self.queue:
            return self.queue
        else:
            return "its empty"
q=Queue_Implementation()
q.enqueue(81)
q.enqueue(28)
q.enqueue(83)
print(q.peek())
print(q.display())
q.dequeue()
print(q.display())