from stack import Stack

base = int(input("Enter the base in which you want the decimal number to convert"))
number = int(input("Enter the decimal number"))

def convert(num):
	list = Stack()
	num = int(num)
	while (num > 0):
		list.push(num%base)
		# print list
		num = num // base

	binary = ''
	while not list.isEmpty():
		binary += str(list.pop())
	return binary
		# 
		


print convert(number) 
