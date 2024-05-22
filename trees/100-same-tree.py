from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Cases:
    #  - both are empty nodes - True 
    #  - both are not empty and are same value - True 
    #  - both are not empty and not same value - False 
    #  - one is None and another has value - False 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



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

print(Solution().isSameTree(tree1, tree2))   