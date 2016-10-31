class Queue:
	def __init__(self):
		self.item = []
		

	def enqueue(self,num):
		return self.item.insert(0,num)

	def isEmpty(self):
		return self.item == []

	def dequeue(self):
		return self.item.pop()

	def size(self):
		return len(self.item)


