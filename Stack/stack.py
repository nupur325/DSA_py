#Stack implementation using linked list
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self,new_node):
        new_node.next = self.top 
        self.top =new_node

    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack contains...")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

st = Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.print()