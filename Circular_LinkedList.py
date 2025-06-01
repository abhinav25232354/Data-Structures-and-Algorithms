class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Circular link
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    def deleteFromBeginning(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def deleteFromEnd(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        prev = None
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        result = []
        temp = self.head
        while True:
            result.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" → ".join(result) + " → (back to head)")

    def length(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count


cll = CircularLinkedList()
cll.insertAtEnd(10)
cll.insertAtEnd(20)
cll.insertAtEnd(30)
cll.insertAtBeginning(5)

cll.display()        # 5 → 10 → 20 → 30 → (back to head)
print("Length:", cll.length())  # Length: 4

cll.deleteFromBeginning()
cll.display()        # 10 → 20 → 30 → (back to head)

cll.deleteFromEnd()
cll.display()        # 10 → 20 → (back to head)
