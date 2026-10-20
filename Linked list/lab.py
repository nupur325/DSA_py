class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_node):
        if (self.head==None):
            self.head=new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

    def insert(self,new_node,pos):
        temp =self.head
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return 
        else:
            p = 1
            while(p!=pos-1 and temp.next!= None):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node
            return

    def alt_del(self):
        prev = self.head
        temp = self.head.next
        while temp and prev:
            prev.next = temp.next
            temp = None
            prev = prev.next
            if prev:
                temp = prev.next

    def print(self):
        temp = self.head
        print("\nLinkedList:")
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next

list=LinkedList()
list.append(Node(21))
list.append(Node(43))
list.append(Node(32))
list.print()
list.insert(Node(100),3)
list.print()
list.alt_del()
list.print()