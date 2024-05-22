from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left

        return root
        

        

root = TreeNode(8)
root.left = TreeNode(13)
# root.left.left = TreeNode(11)
root.right = TreeNode(4)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)

targetSum = 20  # T
# targetSum = 0  # T
# targetSum = 21  # [[8, 13]]

print(Solution().pathSum(root, targetSum))
