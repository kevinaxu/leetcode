from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:

    def invert(self, root) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left 
        return root

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, self.invert(root.right))


# Tree 1
#       1
#    /    \
#   2      2
#    \       \
#      3      3
a = TreeNode(3)
b = TreeNode(11)
c = TreeNode(8)
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

result = Solution().invert(tree1)
print(preorderIterative(result))