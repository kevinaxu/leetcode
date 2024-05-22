from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Can we do better? Instead of getting the values and sorting
    # T: O(n) 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left, right = float("-inf"), float("inf")
        return self.dfs(root, left, right)

    def dfs(self, root, left_bounds, right_bounds) -> bool:
        if not root:
            return True

        curr = left_bounds < root.val and root.val < right_bounds
        left = self.dfs(root.left, left_bounds, root.val) if root.left else True            
        right = self.dfs(root.right, root.val, right_bounds) if root.right else True            

        return left and right and curr


    # # DFS / Iterative - In-Order
    # # T: dfs() + sort + set --> O(n) + O(nlog(n)) + O(n) --> O(nlog(n))
    # # NOTE: We can easily improve this to O(n) by iterating over array to check strict sort with early exit
    # # S: O(n) to store values 
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     values = self.dfsInorder(root)
    #     return values == sorted(values) and len(values) == len(set(values))

    # def dfsInorder(self, root):
    #     values, stack = [], []
    #     while root or stack:
    #         if root:
    #             stack.append(root)
    #             root = root.left
    #         else:
    #             curr = stack.pop()
    #             values.append(curr.val)
    #             root = curr.right
    #     return values



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

print(Solution().isValidBST(tree1))   


'''
# DFS / Recursive - Base Case: Empty Tree
# WRONG - see Test Case 
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    if not root:        # Empty tree is valid
        return True 

    # check subtrees 
    is_bst_left = self.isValidBST(root.left)
    is_bst_right = self.isValidBST(root.right) 

    # check current node - 3 conditions (1 child, no child, 2 child)
    left = (root.left.val < root.val) if root.left else True 
    right = (root.val < root.right.val) if root.right else True 

    # root is BST if all conditions are met 
    return is_bst_left and is_bst_right and left and right 
'''