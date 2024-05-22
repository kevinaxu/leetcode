from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # DFS / recursive - only look at right side
    # NOTE: this implementation won't work on Tree 2 (see below)
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     right = self.rightSideView(root.right)      # leap of faith... [4]
    #     return [root.val, *right]


    # BFS / iterative - go level by level, only take the right most (eg last node of the level)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        values, res = [], []
        num_nodes_in_level = 1
        queue = deque([ root ])
        while queue:
            curr = queue.popleft()
            values.append(curr.val)

            # Enqeueu
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            num_nodes_in_level -= 1 
            if num_nodes_in_level == 0:
                res.append(values.pop())        # append LAST element in level 
                values = [] 
                num_nodes_in_level = len(queue)

        return res 


# Tree 2
#       3
#    /    \
#   11     4
#  /  \     
# 4    3
# Expected: [3, 4, 3]

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

print(Solution().rightSideView(tree1))   # [3,4,4]