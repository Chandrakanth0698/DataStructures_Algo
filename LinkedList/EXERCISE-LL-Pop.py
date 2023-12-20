class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            # print("Empty linked List")
            return None
        elif self.head.next is None:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            popped_node = self.tail
            self.tail = temp
            self.tail.next = None
            self.length -= 1
            return popped_node



my_linked_list = LinkedList(1)
my_linked_list.append(2)
#my_linked_list.print_list()
# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""