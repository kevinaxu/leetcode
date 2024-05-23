from typing import Optional, List
from collections import deque

# DFS / iterative 
# def has_path(graph, src, dst):
#     stack = [ src ] 
#     while stack:
#         curr = stack.pop()
#         if curr == dst:
#             return True 
#         for neighbor in graph[curr]:
#             stack.append(neighbor)
#     return False 

# DFS / recursive
# def has_path(graph, src, dst) -> bool:
#     if src == dst:
#         return True 
#     for neighbor in graph[src]:     # Recursive Leap of Faith... this will return T / F 
#         if has_path(graph, neighbor, dst):
#             return True 
#     return False 

# BFS / iterative 
def has_path(graph, src, dst) -> bool: 
    queue = deque([ src ])
    while queue: 
        curr = queue.popleft()
        if curr == dst:
            return True 
        for neighbor in graph[curr]:
            queue.append(neighbor)
    return False 

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True