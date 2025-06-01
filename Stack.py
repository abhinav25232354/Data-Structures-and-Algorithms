# Stack is a data structure which works on principle of LIFO (Last In First Out)

# Diagram
"""
|--5--|
|--4--|
|--3--|
|--2--|
|--1--|
|--0--|
[-----]
"""
"""
functions:
push(): for inserting new value to the stack
pop(): take out the last inserted value from the stack
""" 

class Stack:
    def __init__(self, array=None):
        self.array = array if isinstance(array, list) else []

    def push(self, value):
        try:
            self.array.append(value)
            return f"Pushed: {value}"
        except Exception as e:
            print(e)

    def pop(self):
        try:
            if self.array:
                return f"Popped: {self.array.pop()}"
            else:
                return "Stack is empty"
        except Exception as e:
            print(e)

    def peek(self):
        try:
            return self.array[-1]
        except Exception as e:
            print(e)
    
    def isEmpty(self):
        try:
            if len(self.array) == 0:
                return "Stack is Empty"
            else:
                return f"Stack is not empty. It has {len(self.array)} elements."
        except Exception as e:
            print(e)
    
    def size(self):
        try:
            return len(self.array)
        except Exception as e:
            print(e)
            
array_1 = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array_1.push(11))
print(array_1.array)
print(array_1.pop())
print(array_1.array)
print(array_1.peek())
print(array_1.array)
print(array_1.isEmpty())
print(array_1.size())