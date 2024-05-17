# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        # traverse through both trees - at the same time? 
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":

    # Construct a sample tree
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(4)
    t2.left.left = TreeNode(4)

    print(Solution().isSameTree(t1, t2))