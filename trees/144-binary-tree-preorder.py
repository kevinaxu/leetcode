from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # # DFS / Recursive / Preorder
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     def traverse(root):
    #         if root:
    #             values.append(root.val)
    #             traverse(root.left)
    #             traverse(root.right)
    #     values = [] 
    #     traverse(root)
    #     return values

    # DFS / Iterative / Preorder
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        values, stack = [], [ root ]
        while stack:
            curr = stack.pop()
            values.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return values      

# Tree 1
#       3
#    /    \
#   11     4
#  /       
# 4   
a = TreeNode(3)
b = TreeNode(11)
c = TreeNode(4)
d = TreeNode(4)
a.left = b
a.right = c
b.left = d
tree1 = a


print(Solution().preorderTraversal(tree1))   