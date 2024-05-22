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
    # keep track of:
    # - number of nodes in the level we still need to process
    # - value of nodes at each level 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        values, res = [], [] 
        num_nodes_in_level = 1
        queue = deque([ root ])
        while queue:
            curr = queue.popleft()

            values.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            num_nodes_in_level -= 1 
            if num_nodes_in_level == 0:

                # add the values in the level to the results 
                res.append(values)
                values = []

                # update the num_nodes in level - len(queue)
                num_nodes_in_level = len(queue)

        return res


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

print(Solution().levelOrder(a))     # [[3], [11, 4]]
