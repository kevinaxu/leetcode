from typing import Optional, List
from collections import deque

# DFS / Iterative
# Time Complexity: O(1) add / remove elemenets. O(n) total 
# def dfs(graph, start) -> List[str]:
#     values, stack = [], [ start ]           # stack is going to contain keys
#     while stack:
#         key = stack.pop()       # a
#         values.append(key)
#         curr = graph[key]       # [b, c]
#         for node in curr:
#             stack.append(node)
#     return values 

# DFS / Recursive
# No explicit base case! 
# What is a base case? --> The absence of a recursive case 
# Base Case ~ absense of a recursive case
# # Time Complexity: O(1) add / remove elemenets. O(n) 
# Space Complexity: O(n) - linear based on time 
# def dfs(graph, current) -> None:
#     print(current)
#     for neighbor in graph[current]:
#         dfs(graph, neighbor)

# Time Complexity: O(1) add / remove elemenets. O(n) 
# Space Complexity: O(n) - linear based on time 
def bfs(graph, start) -> List[str]:
    values, queue = [], deque([ start ])
    while queue:
        current = queue.popleft()
        values.append(current)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
    return values 

'''
BFS 
'''

# BFS / iterative - iterate over all nodes in current level (similar to trees BFS) 
# Input: adjacency list 
# Returns:
#   -1 if no src == 1
#   number of iterations to get to src
def bfs(graph, src, dest):
    visited, queue = set(), deque([ src ])
    level = 0
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr in visited: continue
            if curr == dest: return level
            visited.add(curr)
            for neighbor in graph[curr]:
                queue.append(neighbor)
        level += 1
    return -1





# DFS - get topological ordering 
def topological_sort(graph):
    nodes = graph.keys()
    num_nodes = len(nodes)

    order, visited = [], set()

    def dfs(node):
        print("processing:", node)
        # Base Case: 
        if node in visited:
            print("already visited, skipping...", node)
            return 

        visited.add(node)
        if not graph[node]:     # add to top ordering
            order.append(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    dfs("F")

    print("visited", visited)


graph = {
  "J": ["M", "L"],
  "K": ["J"],
  "F": ["K", "J"],
  "H": ["J, I"],
  "L": [],
  "M": [],
  "I": ["L"],
  "G": ["I"],
  "D": ["H", "G"],
  "E": ["A", "D", "F"],
  "A": ["D"],
  "C": ["B", "A"],
  "B": ["D"]
}
topological_sort(graph)