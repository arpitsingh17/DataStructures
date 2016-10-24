class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
        return self.items == []

     def size(self):
        return len(self.items)

     def push(self, item):
         return self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]



s1 = Stack()
s1.push(1)
s1.push(2)
print s1
print s1.size()
print s1.pop()
print s1.isEmpty()
print s1.peek()
