# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        result = float("-inf")

        def dfs(root):
            nonlocal result
            if root is None: return 0

            left, right = dfs(root.left), dfs(root.right)
            left, right = max(left, 0), max(right, 0)

            path_sum = root.val + left + right
            if path_sum > result: result = path_sum

            return root.val + max(left, right)

        dfs(root)
        return result

if __name__ == "__main__":

    # Construct a sample tree
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)

    print(Solution().maxPathSum(t1))