

# Will both traversal types return the paths? 
# YES, but DFS may search in a totally wrong direction 
# BFS - explores directions very evenly 

# TODO
# check for cycles - return -1 if there's no path that exists
# only add to queue if we haven't seen the node
# Time: O(n)


from collections import deque

def build_adjacency_list(edges) -> dict:
    adj = {}
    for k, v in edges:
        if k not in adj: adj[k] = [] 
        if v not in adj: adj[v] = [] 
        adj[k].append(v)
        adj[v].append(k)
    return adj


# TODO
# instead of passing in (neighbor, distance)
# are we able to keep track of which level we're on from a global level? 
# see Shortest Bridge (https://www.youtube.com/watch?v=gkINMhbbIbU)
def bfs(graph, src, dest):
    visited, queue = set(), deque([ src ])
    level = 0
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr in visited:
                continue
            if curr == dest:
                return level
            visited.add(curr)
            for neighbor in graph[curr]:
                queue.append(neighbor)
        level += 1
    return -1

def shortest_path(edges, node_A, node_B):
    graph = build_adjacency_list(edges)
    return bfs(graph, node_A, node_B)

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
print(shortest_path(edges, 'w', 'z')) # -> 2





# def bfs(graph, src, dest):
#     visited, queue = set(), deque([ (src, 0) ])
#     while queue:
#         curr, num_edges = queue.popleft()
#         if curr == dest:
#             return num_edges

#         visited.add(curr)
#         for neighbor in graph[curr]:
#             if neighbor not in visited:
#                 queue.append((neighbor, num_edges + 1))
#     return -1