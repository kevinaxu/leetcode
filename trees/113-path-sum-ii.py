from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        curr = []
        self._pathSum(root, targetSum, curr, results)
        return results

    def _pathSum(self, root, targetSum, curr, res) -> List[List[int]]:
        if root:
            # Base Case: I'm a leaf node and value == targetSum
            if not root.left and not root.right:
                if root.val == targetSum:

                    # Successful path - add it to the curr path, then append to the final res 
                    curr = curr + [root.val]
                    res.append(curr)

            curr = curr + [root.val]
            self._pathSum(root.left, targetSum - root.val, curr, res)
            self._pathSum(root.right, targetSum - root.val, curr, res)
        

    

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

