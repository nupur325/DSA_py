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
            popped_data =  temp.data
            self.top = self.top.next
            temp = None
            return popped_data

    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack contains...")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print()

# Queue implementation using linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, new_node):
        if self.isempty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front:
            temp=self.front
            dequeue_data=temp.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            return dequeue_data
        else:
            return None

    def print(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Queue contains...")
            temp = self.front
            while temp:
                print(temp.data,end = "->")
                temp = temp.next
            print()

def reverse_stack(s1):
    q1 = Queue()
    while not s1.isempty(): #pop from stack and enqueue to queue
        q1.enqueue(Node(s1.pop()))
    #q1.print()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.print()

q = Queue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.print()
q.dequeue()
print("after dequeue")
q.print()

st = Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.print()
st.pop()
print("After pop:")
st.print()
reverse_stack(st)