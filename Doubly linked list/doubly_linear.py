#Doubly linear linked list
class Node:
    def __init__(self,value):
        self.prev = None
        self.data = value 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_node):
        temp = self.head
        if temp:
            while temp.next:    #finding last node
                temp = temp.next
            temp.next = new_node    #append
            new_node.prev = temp
        else:   #First node
            self.head = new_node

    def print(self):
        temp = self.head
        print("List elements: ")
        while temp:
            print(temp.data,end = " ")
            temp = temp.next

list=LinkedList()
list.append(Node(12))
list.append(Node(52))
list.append(Node(22))
list.append(Node(42))
list.print()