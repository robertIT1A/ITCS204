class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

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
preOrderTraversal(root)