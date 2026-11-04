class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack Underflow")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next

    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack contains...")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    def reverse_string(self, s):
        temp = Stack()
        for ch in s:
            temp.push(Node(ch))
        rev = ""
        while not temp.isempty():
            rev += temp.top.data
            temp.pop()
        print("Reversed string:", rev)

    def reverse_stack(self):
        temp = Stack()
        while not self.isempty():
            temp.push(Node(self.top.data))
            self.pop()
        while not temp.isempty():
            self.push(Node(temp.top.data))
            temp.pop()
        print("Stack reversed successfully")


st = Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))

st.display()

st.pop()

print("After pop:")
st.display()

st.reverse_string("PYTHON")

st.reverse_stack()

print("After reversing stack:")
st.display()