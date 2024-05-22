from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        '''
        Why Can't we use empty tree as the base case? 
        Input: root = [], targetSum = 0 --> there exists no path in the empty tree to sum to anything! 
        '''
        # Base Case: I'm a Leaf node and I'm equal to the target! 
        if not root.left and not root.right:
            if root.val == targetSum:
                return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


# root = [5,4,8,11,null,13,4,7,2,null,null,null,1]

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

# root = None

# targetSum = 20  # T
# targetSum = 0  # T
targetSum = 21  # F 

print(Solution().hasPathSum(root, targetSum))

