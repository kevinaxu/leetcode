# Definition of binary tree node.
class TreeNode: 
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def bfs_iterative(root):
    if root is None: return []

    queue = [root]
    results = []

    while len(queue) > 0:
        curr = queue.pop(0)
        results.append(curr.val)

        if curr.left: queue.append(curr.left)
        if curr.right: queue.append(curr.right)
    return results



class Solution: 
    def invertTree(self, root):
        # DFS (recursive)
        if root is None: return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.right)

        self.invertTree(root.left)

        return root

        # BFS (Iterative, Queue) 
        # Instead of printing out results, we want to instead construct a new tree
        # NOTE: Output needs to be root node so this approach doesn't work! 
        #
        # if root is None: return []
        # q = [root]          # Queue
        # result = []
        # while len(q) > 0:
        #     curr = q.pop(0)
        #     result.append(curr.val)

        #     if curr.right: q.append(curr.right)
        #     if curr.left: q.append(curr.left)

        # return result



if __name__ == "__main__":

    # Construct a sample tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    inverted = Solution().invertTree(root)
    print(bfs_iterative(inverted))