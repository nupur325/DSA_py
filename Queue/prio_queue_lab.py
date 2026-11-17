class Node:
    def __init__(self,patientId,name,pr):
        self.pid = patientId
        self.name = name
        self.priority = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self,newNode):
        if self.front == None:
            self.front = newNode
            return 
        if self.front.priority>newNode.priority:
            newNode.next = self.front
            self.front = newNode
            return
        
        temp = self.front
        while temp and newNode.priority>= temp.priority:
                prev = temp
                temp = temp.next
        prev.next = newNode
        newNode.next = temp
        if temp == None:
            self.rear = newNode

    def display_next(self):
        if self.front == None:
            print("Queue is empty")
        else:
            print("Next patient:")
            print(self.front.pid,self.front.name,self.front.priority)

    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Patient treated:",temp.pid,temp.name)
            self.front = self.front.next

            if self.front == None:
                self.rear = None

    def display_all(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Waiting patients:")
            while temp:
                print(temp.pid,temp.name,temp.priority)
                temp = temp.next

pq = PriorityQueue()
pq.enqueue(Node(101,"Nupur",2))
pq.enqueue(Node(102,"Sam",1))
pq.enqueue(Node(103,"Nups",3))
pq.enqueue(Node(104,"Samuel",1))
pq.enqueue(Node(105,"Shree",5))
pq.enqueue(Node(106,"Sai",4))
pq.display_all()
pq.display_next()
pq.dequeue()
print("After")
pq.display_all()