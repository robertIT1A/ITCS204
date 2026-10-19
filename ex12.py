class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")

root = TreeNode('G')
nodeA = TreeNode('U')
nodeB = TreeNode('E')
nodeC = TreeNode('V')
nodeD = TreeNode('A')
nodeE = TreeNode('R')
nodeF = TreeNode('R')
nodeG = TreeNode('A')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
print("Postorder Traversal")
postOrderTraversal(root)
