# class Stack(object):
# 	def __init__(self):
# 		self.array = []

# 	def isEmpty(self):
# 		if self.array == []:
# 			return True
# 		else:
# 			return False

# 	def push(self,data):
# 		self.array.append(data)

# 	def pop(self):
# 		return self.array.pop()

# 	def size(self):
# 		return len(self.array)



# new = Stack()
# print new.isEmpty()
# new.push("asdf")
# new.push("asd")
# new.push("as")

# print new.size()

# print new.pop()
# print new.pop()

# class Queue(object):
# 	def __init__(self):
# 		self.array = []

# 	def enqueue(self,data):
# 		self.array.append(data)

# 	def dequeue(self):
# 		return self.array.pop(0)

# new = Queue()
# new.enqueue(1)
# new.enqueue(2)
# new.enqueue(3)
# new.enqueue(1)
# print new.dequeue()
# print new.dequeue()
# print new.dequeue()
# print new.dequeue()

class Deque(object):
	def __init__(self):
		self.array = []

	def addEnd(self,data):
		self.array.append(data)

	def addFront(self,data):
		self.array.insert(0,data)

	def removeFront(self):
		return self.array.pop(0)

	def removeEnd(self):
		return self.array.pop()

new = Deque()
new.addFront(2)
new.addFront(1)
new.addEnd(3)
new.addEnd(4)

print new.removeFront()	
print new.removeFront()

print new.removeFront()
print new.removeFront()




