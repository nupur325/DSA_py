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
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isempty():
            print("Queue Underflow")
        else:
            temp = self.front
            print("Deleted element:", temp.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Queue contains...")
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next

    def reverse_queue(self):
        st = []
        while not self.isempty():
            st.append(self.front.data)
            self.dequeue()
        while len(st) > 0:
            self.enqueue(Node(st.pop()))
        print("Queue reversed successfully")

    def merge_queue(self, q2):
        merged = Queue()
        temp = self.front
        while temp:
            merged.enqueue(Node(temp.data))
            temp = temp.next
        temp = q2.front
        while temp:
            merged.enqueue(Node(temp.data))
            temp = temp.next

        print("Merged queue:")
        merged.display()

    def identical_queue(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                print("Queues are not identical")
                return
            temp1 = temp1.next
            temp2 = temp2.next
        if temp1 is None and temp2 is None:
            print("Queues are identical")
        else:
            print("Queues are not identical")


q1 = Queue()

q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(30))
q1.enqueue(Node(40))

q1.display()

q1.dequeue()

print("After dequeue:")
q1.display()

q1.reverse_queue()

print("After reversing queue:")
q1.display()

q2 = Queue()
q2.enqueue(Node(50))
q2.enqueue(Node(60))

print("Merging queues:")
q1.merge_queue(q2)

print("Checking identical queues:")
q1.identical_queue(q2)
