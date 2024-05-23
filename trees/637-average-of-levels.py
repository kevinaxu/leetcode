from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # BFS / iterative
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        values, queue = [], deque([ root ])

        while queue:
            level = [] 
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            values.append(sum(level) / len(level))
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

print(Solution().averageOfLevels(tree1))        # [3, 14.5, 11] floats 