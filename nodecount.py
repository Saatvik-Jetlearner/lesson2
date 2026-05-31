class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def count_nodes(root):
    if root == None:
        return "No Nodes"
    
        
root = TreeNode(10)
root.leftNode = TreeNode(5)
root.rightNode = TreeNode(15)
print("Total Nodes: ", count_nodes(root))



