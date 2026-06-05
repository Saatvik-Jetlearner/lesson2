class TreeNode:
    def __init__(self, x):
        self.data = x
        self.leftChild = None
        self.rightChild = None

def InOrderTraversal(root):
    if root is not None:
        if root.leftChild is not None:
                InOrderTraversal(root.leftChild)
        print(root.data)
        if root.rightChild is not None:
                InOrderTraversal(root.rightChild)

def Insert(root, k):
    if root == None:
            return TreeNode(k)
    if root.data > k:
            root.leftChild = Insert(root.leftChild, k)
    else:
            root.rightChild = Insert(root.rightChild, k)
    return root

def InorderSuccesor(root):
    current = root
    while current.leftChild is not None:
        current = current.leftChild
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.leftChild = delete(root.leftChild, key)
    elif key > root.data:
        root.rightChild = delete(root.rightChild, key)
    else:
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
        elif root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp
        else:
             temp = InorderSuccesor(root)
             print("Hello", temp.data)
             t = root.data
             root.data = temp.data
             temp.data = t
             root.rightChild = delete(root.rightChild, temp.data)

n = int(input("Enter the number of elements you want in the tree - "))
root = None
for i in range(n):
    x = int(input("Enter the node value - "))
    root = Insert(root, x)

InOrderTraversal(root)