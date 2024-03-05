class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_element_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_element_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            start = self.head
            while start.next is not None:
                start = start.next
            start.next = new_node

    def add_after_give_element(self, data, prev_ele):
        if self.head is None:
            print('LL is empty')
        else:
            start = self.head
            while start is not None:
                if start.data == prev_ele:
                    break
                start = start.next
            if start is None:
                print('The given element is not present in the LL')
            else:
                new_node = Node(data)
                new_node.next = start.next
                start.next = new_node

    def add_before_given_element(self, data, prev_ele):
        new_node = Node(data)
        if self.head is None:
            print('ll is mt')
            return
        else:
            start = self.head
            while start.next is not None:
                if start.next.data == prev_ele:
                    break
                start = start.next
            if start.next is None:
                print('The given element does not exist.')
            else:
                new_node.next = start.next
                start.next = new_node

    def display(self):
        if self.head is None:
            print('ll is empty')
        else:
            start = self.head
            while start is not None:
                print(start.data, end=' --> ')
                start = start.next

ll = LinkedList()
ll.add_element_at_beginning(4)
ll.add_element_at_end(8)
ll.add_element_at_beginning(1)
ll.add_element_at_end(5)
ll.add_after_give_element(3, 4)
ll.add_before_given_element(0, 4)
ll.display()