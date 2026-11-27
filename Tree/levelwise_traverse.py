#level order traversal
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,newNode):
        if self.root == None:
            self.root = newNode
            return
        else:
            temp = self.root
            while True:
                if newNode.data < temp.data:    #left subtree
                    if temp.left is None:
                        temp.left = newNode
                        return
                    else:
                        temp = temp.left
                else:                   #right subtree
                    if temp.right is None:
                        temp.right = newNode
                        return
                    else:
                        temp = temp.right

    def inorder(self,temp):          #recursive
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)

    def level_order_traversal(self,rt):
        if rt is None:
            print("BST is empty")
        arr = []
        cnt = 0 #for counting visited nodes
        level = 0
        arr.append(rt)
        while cnt<len(arr):
            node_count = len(arr)-cnt   #no of nodes to be visited
            print("\n Level: ",level, ' nodes',end = " ")
            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1
                print(temp.data, end = " ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level += 1
        print("\nHeight of the tree",level-1)

btree = BST() 
btree.insert(Node(100))
btree.insert(Node(10))
btree.insert(Node(450))
btree.insert(Node(4))
btree.insert(Node(65))
btree.insert(Node(300))
btree.insert(Node(500))
btree.insert(Node(50))
btree.inorder(btree.root)
print("\nLevel order")
btree.level_order_traversal(btree.root)
