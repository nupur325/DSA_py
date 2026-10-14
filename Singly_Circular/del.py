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
            new_node.next = self.head  #circular list 
        else:
            temp=self.head
            while(temp.next!= self.head):
                temp=temp.next
            temp.next=new_node #apppending new node
            new_node.next = self.head   #again circular list

    def insert(self,new_node,pos):
        if pos == 1:
            temp = self.head
            while(temp.next!=self.head):
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
        else:
            p = 1
            temp = self.head
            while(p!=pos-1):
                temp = temp.next
                p+=1
            new_node.next = temp.next
            temp.next = new_node
            return

    def delete(self,value):  
        temp = self.head
        prev = None
        if temp.data == value:  #first node to delete
            while(temp.next!= self.head):  
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
        else:
            while(temp.data!= value and temp):
                prev = temp
                temp = temp.next
                if temp == self.head:
                    print("Value is not present in the list")
                    return
            prev.next = temp.next
            temp = None

    def print(self):
        print()
        print("List elements:")
        temp=self.head
        while(True):
            print(temp.data,end=" ")
            temp=temp.next
            if temp == self.head:
                break

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.append(Node(100))
list.insert(Node(35),4)
list.print()
list.delete(10)
list.print()