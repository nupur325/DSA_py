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
            temp=self.head #assign temp
            while(temp.next):
                temp=temp.next
            temp.next=new_node #apppending new node

    def insert(self, new_node,pos):   #insert node at first position 
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        else:
            p=1
            while(p!=pos-1 and temp.next!=None):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
            return

    def del_node(self, value):
        temp = self.head
        #deleting first node
        if temp.data==value: #searching value
            self.head=self.head.next
            return
        while(temp):
            if temp.data==value:
                break
            else:     #traversing
                prev=temp
                temp=temp.next
            if temp==None:
                print("Value is not there in the list")
            prev.next=temp.next
            temp=None

    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev
    
    def print(self):
        temp=self.head
        print("Linked list data:")
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
#list.insert(Node(130),4)
#list.print()
#list.del_node(100)
#list.print()
list.reverse()
print("Reversed")
list.print()