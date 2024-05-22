from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values, stack = [], [] 
        while root or stack:
            if root:
                stack.append(root)
                root = root.left 
            else: 
                curr = stack.pop()
                values.append(curr.val) 
                root = curr.right 
        return values[k-1] 

# Test Case: valid BST in subtree but not Globally! 
#       5
#    /    \
#   4      6
#         / \
#        3   7
a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(6)
d = TreeNode(3)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
tree1 = a

k = 2

print(Solution().kthSmallest(tree1, k))    # 5