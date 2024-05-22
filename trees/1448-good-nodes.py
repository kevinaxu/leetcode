from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # DFS / recursive
    # Key Intuition:
    # - if the given root is None, there are no good nodes
    # - otherwise:
    #   - check if given root is a good node (root.val < max)
    #   - check good nodes in left subtree
    #   - check good nodes in right subtree
    #   - return total number of good nodes
    def goodNodes(self, root: TreeNode) -> int:

        def bfs(root, curr_max) -> int:
            nonlocal count
            if root:
                if root.val >= curr_max:
                    count += 1
                    curr_max = root.val

                bfs(root.left, curr_max)      # leap of faith... num good nodes in left subtree
                bfs(root.right, curr_max)
        
        count = 0
        bfs(root, root.val)
        return count



        


# Tree 1
#       3
#    /    \
#   1      4
#  /      / \
# 3      1   5   
a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)
d = TreeNode(3)
e = TreeNode(1)
f = TreeNode(5)
a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
tree1 = a

print(Solution().goodNodes(tree1))      # 4 