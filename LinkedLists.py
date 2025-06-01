# Linked Lists are also a type of data structure used for efficient array value storage
"""
Two types of linked Lists
1. Singly linked List (address of next element is stored to first element's first half)
2. doubly linked list (address of both next and previous element address is stored with every indiviual element)
3. circular linked list (same as singly linked list but the last element's address is not empty its the address of first element again which makes a circular flow)
"""
"""
Functions
1. insertAtBeginning
2. insertAtEnd
3. deleteFromBeginning
4. deleteFromEnd
5. length
6. search
7. display
Note: data and next are two childNodes of the rootNode
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def deleteFromBeginning(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next
            
    def deleteFromEnd(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                return f"Found at index {index}"
            temp = temp.next
            index += 1
        return "Not found"
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")
    
# Usage
l = SinglyLinkedList()
l.insertAtBeginning(88)
l.insertAtBeginning(75)
l.insertAtBeginning(55)
l.insertAtBeginning(42)
l.insertAtEnd(99)

l.display()                        # 42 → 55 → 75 → 88 → 99 → None
print("Length:", l.length())      # Length: 5
print(l.search(75))               # Found at index 2
l.deleteFromBeginning()
l.deleteFromEnd()
l.display()                        # 55 → 75 → 88 → None