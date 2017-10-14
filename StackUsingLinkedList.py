# This is an implementation of stack using Linked List

class Node(object):
    def __init__(self,value=None,pointer=None):
        self.value = value
        self.pointer = pointer

class Stack(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return not bool(self.head)

    def push(self,item):
        self.head = Node(item,self.head)

    def peak(self):
        if self.head:
            return self.head.value
        else:
            print "Stack is Empty"

    def pop(self):
        if self.head:
            node = self.head
            self.head = node.pointer
            return node.value
    def size(self):
        node = self.head
        count = 0

        while node:
            count += 1
            node = node.pointer
        return count



newstack = Stack()
for i in range(10):
    newstack.push(i)

print "is the stack empty",newstack.isEmpty()
print "Stack size is",newstack.size()
for i in range(10):
    print "newstack poped:",newstack.pop()
