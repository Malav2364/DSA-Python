#practical-4 

class C_Q: 
    def __init__(self,k) :
        self.k=k 
        self.head=-1
        self.tail=-1
        self.q=[None]*self.k
    def enqueue(self,data):
        if self.head==-1 and self.tail==-1:
            self.head=0
            self.tail=0
            self.q[self.tail]=data
        elif (self.tail+1)%self.k==self.head:
            print("Queue is full. element, you tried to insert is failed.",data)
        else:
            self.tail=(self.tail+1)%self.k
            self.q[self.tail]=data
    def dequeue(self):
        if self.head==-1 and self.tail==-1:
            print("Queue is empty. No deletion can be performed")
        elif self.head==self.tail:
            print("The element that is deleted is: ",self.q[self.head])
            self.head=-1
            self.tail=-1
        else: 
            print("the element that is deleted is : ",self.q[self.head])
            self.head=(self.head+1)%self.k
    def front(self):
        if self.head==-1:
            print("queue is empty")
        else:
            return self.q[self.head]
    def rear(self):
        if self.head==-1:
            print("queue is empty")
        else:
            return self.q[self.tail]
    def display(self):
        if self.head==-1 and self.tail==-1:
            print("Queue is empty")
        else:
            start=self.head
            while True:
                print(self.q[start],end='-')
                if start == self.tail:
                    break
                start = (start + 1) % self.k
q=C_Q(5)
q.enqueue(4)
q.enqueue(6)
q.enqueue(3)
q.dequeue()
q.enqueue(2)
q.enqueue(1)
print("The front element is: ",q.front())
print("The front element is: ",q.rear())
q.display()