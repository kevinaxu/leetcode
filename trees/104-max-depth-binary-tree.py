from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # BFS / iterative
    def maxDepth(self, root: Optional[Node]) -> int:
        if not root:
            return 0 
        queue = deque([ root ])

        num_nodes_in_level = 1 
        max_depth = 0 

        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            # here is where we update all vars
            num_nodes_in_level -= 1      # going to nexzt level
            if num_nodes_in_level == 0:
                max_depth += 1
                num_nodes_in_level = len(queue)

            print(f"node: {curr.val}, num nodes in level remaining: {num_nodes_in_level}, max depth: {max_depth}")

        return max_depth 


    # # DFS / recursive
    # def maxDepth(self, root):
    #     if not root: return 0
    #     left_max = self.maxDepth(root.left)       # leap of faith... 2
    #     right_max = self.maxDepth(root.right)     # leap of faith... 1 
    #     return max(left_max, right_max) + 1


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)

a.left = b
a.right = c
# b.left = d

#       3
#    /    \
#   11     4
#  /       
# 4        

print(Solution().maxDepth(a))