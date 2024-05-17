# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):

        if root is None:
            return False
        
        stack = [(root, targetSum)]
        while len(stack) > 0:
            curr, sum = stack.pop()

            if curr.left is None and curr.right is None and curr.val == sum:
                return True

            sum -= root.val
            if curr.left:
                stack.append((root.left, sum))
            if curr.right:
                stack.append((root.right, sum))
        return False

    # Recursive DFS 
    # def hasPathSum(self, root, targetSum):
    #     # Base Case - empty Node
    #     if root is None:
    #         return False

    #     if root.left is None and root.right is None and root.val == targetSum:
    #         return True

    #     return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

if __name__ == "__main__":

    # Construct a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.left.right.right = TreeNode(6)

    print(Solution().hasPathSum(root, 4))