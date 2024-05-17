# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        def dfs(root):
            if root is None: return 0
            return max(dfs(root.left), dfs(root.right)) + 1
    
        return dfs(root)
            
    
if __name__ == "__main__":

    # Construct a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    print(Solution().maxDepth(root))