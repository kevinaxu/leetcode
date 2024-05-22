from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pass


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

# Tree 2
#   11
#  /       
# 4   
q = TreeNode(11)
r = TreeNode(4)
q.left = r
tree2 = q 

print(Solution().isSubtree(tree1, tree2))   