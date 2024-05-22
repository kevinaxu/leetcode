from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        preorder_right = preorder[mid+1:]
        inorder_right = inorder[mid+1:]

        end = len(preorder) - len(preorder_right)
        preorder_left = preorder[mid:end]
        inorder_left = inorder[:mid]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        print("mid", mid)
        print("end", end)
        print("root", root.val)
        print("right subtree")
        print("p:", preorder_right)
        print("i:", inorder_right)
        print("left subtree")
        print("p:", preorder_left)
        print("i:", inorder_left)
        return root 







# This doesn't work! 
#       1
#     /    
#    2     
#   /       
#  3   
preorder = [1, 2, 3]
inorder = [3, 2, 1]

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]


tree = Solution().buildTree(preorder, inorder)

preorder_out = preorderTraversal(tree)
inorder_out = inorderRecursive(tree)
print("p:", preorder_out)
print("i:", inorder_out)


