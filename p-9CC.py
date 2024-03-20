class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def swap_pairs(self):
        temp = self.head
        while temp is not None and temp.next is not None:
            temp.data, temp.next.data =temp.next.data, temp.data
            temp = temp.next.next
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    print()
if __name__ == "__main__":

    llist = LinkedList()
    for i in range(7,0,-1):
        llist.push(i)
    
    print("Original Linked List:")
    llist.print_list()
    llist.swap_pairs()
    print("Linked List after pairwise swapping:")
    llist.print_list()