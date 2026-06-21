class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:        
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root
    
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.righy,data)
    
    def inorder(self):
        res = []
        self.rinorder(self.root,res)
        return res
    def rinorder(self,root,res):
        if root:
            self.rinorder(root.left,res)
            res.append(root.item)
            self.rinorder(root.right,res)

    def preorder(self):
        res = []
        self.rpreorder(self.root,res)
        return res
    def rpreorder(self,root,res):
        if root:
            res.append(root.item)
            self.rpreorder(root.left,res)
            self.rpreorder(root.right,res)

    def postorder(self):
        res = []
        self.rpostorder(self.root,res)
        return res
    def rpostorder(self,root,res):
        if root:
            self.rpostorder(root.left,res)
            self.rpostorder(root.right,res)
            res.append(root.item)

    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    
    def mx_value(self,temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item



    def delete(self,data):
        self.root = self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None: #empty list
            return root 
        if data < root.item: #
            root.left = self.rdelete(root.left,data)
        elif data > root.item:
            root.right = self.rdelete(root.right,data)
        else:
            # Case 1: No left child
            if root.left is None:
                return root.right
            # Case 2: No right child
            elif root.right is None:
                return root.left
            # both child
            root.item = self.min_value(root.right)
            self.rdelete(root.right,root.item)  #Successor 
            # root.item = self.mx_value(root.left)
            #self.rdelete(root.left,root.item) #Predecessor
        return root
    
    def size(self):
        return len(self.inorder())
    




l = BST()
l.insert(50)
l.insert(30)
l.insert(70)
l.insert(10)
l.insert(10)
l.insert(40)
l.insert(60)
l.insert(35)
l.insert(45)

print(l.inorder())
print(l.postorder())
print(l.preorder())
print(l.search(2))
print(l.delete(35))
print(l.inorder())
print(l.size())
print(l.min_value(l.root))
print(l.mx_value(l.root.right))