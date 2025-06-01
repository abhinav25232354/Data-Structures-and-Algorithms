# Queue is a data structure which works on principle of FIFO (First In First Out)
"""
functions-
enqueue: add element in the queue
dequeue: remove first element from the queue
peek: see first element of the queue without removing it
isEmpty: check if queue is empty or not
size: size of the queue
display: shows whole queue at once for clarity
"""
class Queue:
    def __init__(self, elements):
        try:
            self.elements = elements
        except Exception as e:
            print(e)
    
    def enqueue(self, value):
        try:
            self.elements.append(value)
            return f"Enqueued: {value}"
        except Exception as e:
            print(e)
    
    def dequeue(self):
        try:
            if self.elements:
                return f"Dequeued: {self.elements.pop(0)}"  # Remove from the front
            else:
                return "Queue is empty"
        except Exception as e:
            print(e)
    
    def peek(self):
        try:
            return self.elements[0]
        except Exception as e:
            print(e)
    
    def isEmpty(self):
        try:
            if len(self.elements) == 0:
                return "Queue is Empty"
            else:
                return f"Queue is not Empty. It has {len(self.elements)} Elements"
        except Exception as e:
            print(e)
    
    def size(self):
        try:
            return len(self.elements)
        except Exception as e:
            print(e)
    
    def display(self):
        try:
            return self.elements
        except Exception as e:
            print(e)

queue1 = Queue([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(queue1.enqueue(10))
print(queue1.display())
print(queue1.dequeue())
print(queue1.display())
print(queue1.peek())
print(queue1.isEmpty())
print(queue1.size())
print(queue1.display())