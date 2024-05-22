from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # # DFS / Recursive / Inorder: 
    # # Base Case: Empty Tree? 
    # # Basically completely negates having to explictly write checks for empty node! 
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     def traverse(root):
    #         if root:        
    #             traverse(root.left)
    #             values.append(root.val)
    #             traverse(root.right)
    #     values = []
    #     traverse(root)
    #     return values 

    # # DFS / Recursive / Inorder: 
    # def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
    #     values = [] 
    #     def traverse(root):   
    #         if root.left:
    #             traverse(root.left)
    #         values.append(root.val)
    #         if root.right:
    #             traverse(root.right)
    #     if root:
    #         traverse(root)
    #     return values

    # DFS / Iterative / Inorder:
    # T: O(n) where n the number of nodes 
    # S: stack O(m) where m is height of the tree 
    #    values O(n) where n is # nodes
    #       = O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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

# Tree 1
#       3
#    /    \
#   11     4
#  /       
# 5   
a = TreeNode(3)
b = TreeNode(11)
c = TreeNode(4)
d = TreeNode(5)
a.left = b
a.right = c
b.left = d
tree1 = a

print(Solution().inorderTraversal(tree1))   