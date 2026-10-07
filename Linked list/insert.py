#Singly linked list
class Node:
    def __init__(self,val):  #init - special constructor
        self.data=val 
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, new_node):  #everytime i create a new node it has to passed to append
        if(self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node #apppending new node
    def insert(self, new_node,pos):   #insert node at first position 
        if pos==1:
            new_node.next=self.head
            self.head=new_node
        else:
            p==1
            while(p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
    
    def print(self):
        count=0    # count len of list
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.insert(Node(100),1)
list.print()
list.insert(Node(130),4)
list.print()