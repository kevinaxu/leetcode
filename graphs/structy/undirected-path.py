

# Approach 1: Construct Adjacency List from Edges
# potential issues: circular references since it's undirected graph 
# What if the graph has a cycle? 
'''
{
    'i': ['j'],
    'k': ['i', 'l', 'm'],
    'm': ['k'],
    'o': ['n'],
    'j': ['i'],
    'n': ['o'],
    'l': ['k'],
}
'''
def build_adjacency_list(edges) -> dict:
    adj = {}
    for k, v in edges:
        if k not in adj: adj[k] = [] 
        if v not in adj: adj[v] = [] 
        adj[k].append(v)
        adj[v].append(k)
    return adj

def dfs(graph, src, dst) -> bool: 
    visited = set()
    stack = [ src ] 
    while stack:
        curr = stack.pop()
        # print("checking:", curr)
        if curr in visited:
            # print("already checked!")
            continue

        visited.add(curr)
        if curr == dst:
            return True 
        for neighbor in graph[curr]:
            stack.append(neighbor)
    return False 

def undirected_path(edges, src, dest) -> bool:
    graph = build_adjacency_list(edges)
    return dfs(graph, src, dest)


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]


print(undirected_path(edges, 'j', 'm')) # -> True