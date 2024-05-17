# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):

        def dfs(root, targetSum, ls, res):
            if root is None:
                printf("root is None")
                return []

            # Base Case: is Leaf Node and root.val == targetSum
            #   update the path
            #   add the path to the list of results
            if root.left is None and root.right is None and root.val == targetSum:
                ls.append(root.val)
                res.append(ls)
                return

            # Go down both paths until the end
            #   update path with the current root val 
            #   update the sum 
            targetSum -= root.val
            newLs = ls + [root.val]
            
            if root.left:
                dfs(root.left, targetSum, newLs, res)
            if root.right:
                dfs(root.right, targetSum, newLs, res)

        res = []
        dfs(root, targetSum, [], res)

        return res


if __name__ == "__main__":

    # Construct a sample tree
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.left.right.right = TreeNode(6)

    print(Solution().pathSum(root, 1))

    # [[1, 2], [1,3]]

