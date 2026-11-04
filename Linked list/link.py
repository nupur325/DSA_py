class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def append(self,newNode):
        if self.head==None:
            self.head = newNode
        else:
            temp= self.head
            while temp.next!=None:
                temp = temp.next #traversing bhai
            temp.next = newNode

    def print(self):
        temp = self.head
        while temp:
            print(temp.data,id(temp.next), end="-->")
            temp = temp.next
list = LinkedList()
list.append(Node(20))
list.append(Node(30))
list.append(Node(45))
list.append(Node(55))
list.print()