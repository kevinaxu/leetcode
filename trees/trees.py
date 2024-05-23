from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right\



'''
Preorder 
'''
# DFS / Iterative / Preoder
def preorderIterative(root: Optional[TreeNode]) -> List[int]:
    values, stack = [], [ root ]
    while stack:
        curr = stack.pop()
        values.append(curr.val) 
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return values


# DFS / Recursive / Preorder
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def traverse(root):
        if root:
            values.append(root.val)
            traverse(root.left)
            traverse(root.right)
    values = [] 
    traverse(root)
    return values



'''
Inorder 
'''

# DFS / Iterative / Inorder
def inorderIterative(root: Optional[TreeNode]) -> List[int]:
    values, stack = [], [] 
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            curr = stack.pop()
            values.append(curr.val)
            root = curr.right
    return values 

# DFS / Recurisve / Inorder
def inorderRecursive(root: Optional[TreeNode]) -> List[int]:
    def traverse(root):
        if root:        
            traverse(root.left)
            values.append(root.val)
            traverse(root.right)
    values = []
    traverse(root)
    return values 

'''
BFS
'''
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return [] 
    values, queue = [], deque([ root ])
    while queue:
        level = [] 
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        values.append(level)
    return values 






# Tree 1
#       3
#    /    \
#   1      4
#  /      / \
# 3      1   5   
a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)
d = TreeNode(3)
e = TreeNode(1)
f = TreeNode(5)
a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
tree = a


print(preorderIterative(tree))
print(inorderIterative(tree))