from collections import deque

def bfs(graph, start) -> set: 
    visited = set()
    queue = deque([ start ])
    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)
    return visited
    

def largest_component(graph) -> int:
    largest = 0
    while graph:
        start = list(graph.keys())[0]       # get "first" key from dictionary
        visited = bfs(graph, start)         # traverse component 

        largest = max(largest, len(visited))
        for node in visited:                # remove component from graph
            graph.pop(node)

    return largest 


graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}
print(largest_component(graph)) # -> 4