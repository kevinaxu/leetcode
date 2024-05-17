class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if root is None: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# Inorder Traversal
def inorder(root):
    if root is None: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# Postorder Traversal where node values are returned
def postorder(root):
    if root is None:
        return []
    
    left = postorder(root.left)
    right = postorder(root.right)
    return left + right + [root.val]

# DFS / Pre-order / Recursive 
def dfs_recursive(root):
    if root is None:
        return []
    return [root.val] + dfs_recursive(root.left) + dfs_recursive(root.right)

# DFS / Pre-order / Iterative (stack) 
def dfs_iterative(root):
    if root is None: return []

    stack = [root]
    results = []

    while len(stack) > 0:
        current = stack.pop()
        results.append(current.val)
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)

    return results


# Tree Includes
# Input: Binary Tree
# Return: True / False if target value exists



# BFS / Iterative (queue)
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
    


if __name__ == "__main__":

    # Construct a sample tree
    #         1
    #      2    3
    #     4 5
    #        6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    # print(postorder(root))
    print(bfs_iterative(root))

