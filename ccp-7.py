class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        start = self.head
        while start.next:
            start = start.next
        start.next = new_node
        
    def display(self):
        start = self.head
        while start:
            print(start.data, end=" ")
            start = start.next
        
def merge_ll(head1, head2):
    temp_head = Node(0)
    start = temp_head
    while True:
        if head1 is None:
            start.next = head2
            break
        if head2 is None:
            start.next = head1
            break
        if head1.data <= head2.data:
            start.next = head1
            head1 = head1.next
        else:
            start.next = head2
            head2 = head2.next
        start = start.next
        return temp_head.next

LL_1 = LL()
LL_1.insert(5)
LL_1.insert(10)
LL_1.insert(15)

LL_2 = LL()
LL_2.insert(2)
LL_2.insert(3)
LL_2.insert(20)

LL_1.head = merge_ll(LL_1.head, LL_2.head)
print("Merged Linked List: ")
LL_1.display()