# Definition of binary tree node.
class TreeNode: 
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution: 
    def isBalanced(self, root):

        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)

            balance = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            height = 1 + max(left[1], right[1])

            return [balance, height]
        
        return dfs(root)[0]




if __name__ == "__main__":

    # Construct a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    print(Solution().isBalanced(root.left))
