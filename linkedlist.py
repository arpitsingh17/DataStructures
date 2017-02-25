'''The main advantage of using a linked list over a 
similar data structure, like the static array, 
is the linked list’s dynamic memory allocation:
if you don’t know the amount of data you want to store before hand, the linked list can adjust on the fly.* Of course this advantage comes at a price: dynamic memory allocation 
requires more space and commands slower look up times.'''

class Node():
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0

        while current:
            current = current.get_next()
            count += 1
        return count

    def search(self,data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data :
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current






