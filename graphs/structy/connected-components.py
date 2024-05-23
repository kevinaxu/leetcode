from collections import deque

# def dfs(graph, start) -> set:
#     visited = set()
#     stack = [ start ] 
#     while stack:
#         curr = stack.pop()
#         if curr in visited:
#             continue
#         visited.add(curr)
#         for neighbor in graph[curr]:
#             stack.append(neighbor)
#     return visited


def bfs(graph, start) -> set: 
    visited = set()
    queue = deque([ start ])
    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.append(curr)

        for neighbor in graph[curr]:
            queue.append(neighbor)
    return visited
    

def connected_components_count(graph) -> int:
    
    count = 0
    while graph:
        start = list(graph.keys())[0]       # get "first" key from dictionary
        visited = bfs(graph, start)         # traverse component 

        count += 1                          # update component count
        for node in visited:                # remove component from graph
            graph.pop(node)

    return count 


graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}
# print(dfs(graph, 0)) 
print(connected_components_count(graph))  # -> 2