"""
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. 
The elements in a linked list are linked using pointers as shown in the below image:
In simple words, a linked list consists of nodes where each node contains a data field and a reference(link) 
to the next node in the list.
"""


class Node:
    def __init__(self, data: object):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def peek_next(self):
        return self.head.next.data
    
    def peek(self):
        return self.head.data
    
    def next(self):
        self.head = self.head.next

    def add(self, data: object):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)


sll = SinglyLinkedList()
sll.add(1)
sll.add(2)
sll.add(3)

print(sll.peek_next())