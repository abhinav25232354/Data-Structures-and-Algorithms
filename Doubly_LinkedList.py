class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def deleteFromBeginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def deleteFromEnd(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def displayForward(self):
        temp = self.head
        print("Forward: ", end="")
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("None")

    def displayBackward(self):
        if self.head is None:
            print("Backward: None")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        print("Backward: ", end="")
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.prev
        print("None")

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

dll = DoublyLinkedList()
dll.insertAtBeginning(10)
dll.insertAtBeginning(20)
dll.insertAtEnd(5)
dll.insertAtEnd(1)

dll.displayForward()    # Forward: 20 ⇄ 10 ⇄ 5 ⇄ 1 ⇄ None
dll.displayBackward()   # Backward: 1 ⇄ 5 ⇄ 10 ⇄ 20 ⇄ None

print("Length:", dll.length())  # Length: 4

dll.deleteFromBeginning()
dll.deleteFromEnd()

dll.displayForward()    # Forward: 10 ⇄ 5 ⇄ None
