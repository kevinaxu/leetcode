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


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

bfs(graph, "a")