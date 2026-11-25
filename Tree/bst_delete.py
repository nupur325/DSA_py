#delete node where : only right child or only left child
#                   node has both left and right child
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

    def delete_node(self,rt,val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left = self.delete_node(rt.left, val)
        elif val>rt.data:
            rt.right = self.delete_node(rt.right,val)
        else:
            if rt.left is None: #Node with right vhild only
                return rt.right
            if rt.right is None: #Node with left child only
                return rt.left
            #node has both left and right children
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.delete_node(rt.right, succ.data)
        return rt

    def get_successor(self,temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp


    def inorder(self,temp):          #recursive
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)

btree = BST()
btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))
btree.inorder(btree.root)
btree.delete_node(btree.root,10)
print("\nAfter deletion:")
btree.inorder(btree.root)
