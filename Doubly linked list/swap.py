#19 oct
#swap first and last node in doubly linked list
#Doubly linear linked list
#insert node and reverse list operation
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

    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            p = 1
            while(p!=pos-1 and temp.next):
                temp = temp.next
                p+=1
            #temp.next = new_node
            #new_node.prev = temp
            new_node.next = temp.next
            if temp.next:           #for last position
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    def rev(self):
        temp = self.head
        print("\nReverse list")
        while temp.next:
            temp = temp.next
        while(temp):
            print(temp.data,end = " ")
            temp = temp.prev

    def swap(self):
        print("\nAfter Swapping")
        temp = node1 = self.head #node1 is the first node
        while (temp.next): #temp is last node
            temp = temp.next
        temp.next = node1.next
        node1.next = None
        node1.prev = temp.prev
        temp.prev.next = node1
        temp.prev = None
        self.head = temp


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
list.print()
list.insert(Node(37),1)
list.insert(Node(99),5)
list.print()
list.swap()
list.print()
#list.rev()
#list.print()