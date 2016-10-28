from stack import Stack


def convert(num):
	list = Stack()
	num = int(num)
	while (num > 0):
		list.push(num%2)
		# print list
		num = num // 2

	binary = ''
	while not list.isEmpty():
		binary += str(list.pop())
	return binary
		# 
		


print convert(255) 
