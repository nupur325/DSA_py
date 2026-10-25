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
        if self.isempty():
            print("Queue is empty")
        else:
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def print(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Queue contains...")
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next

q = Queue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.print()