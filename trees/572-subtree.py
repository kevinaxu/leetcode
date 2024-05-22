from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[Node], subRoot: Optional[Node]) -> bool:
        if not root:
            return False

        if self.isEqual(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)        # LOF ... 
        right = self.isSubtree(root.right, subRoot)
        return left or right

        

    def isEqual(self, t1, t2):
        # Base Case: Empty trees are equal 
        if not t1 and t2: return False
        if not t2 and t1: return False
        if not t1 and not t2: return True
        
        curr = t1.val == t2.val
        left = self.isEqual(t1.left, t2.left)       # LOF... T / F if substrees are equal 
        right = self.isEqual(t1.right, t2.right)
        return curr and left and right



# Tree 1
#       3
#    /    \
#   11     4
#  /       
# 4   
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
a.left = b
a.right = c
b.left = d
tree1 = a

# Tree 2
#   11
#  /       
# 4   
q = Node(11)
r = Node(4)
q.left = r
tree2 = q 

print(Solution().isEqual(tree1.left, tree2))         # False 