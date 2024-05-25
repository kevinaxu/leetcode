from typing import Optional, List
from collections import deque
from pprint import pprint

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build the Adjacency List
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        top_sort = [] 

        # Init Graph and Incoming Degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Init the queue with all courses with indegree == 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            top_sort.append(curr)

            for next_course in graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return top_sort if len(top_sort) == numCourses else []
    

numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
print(Solution().canFinish(numCourses, prerequisites))





''' 
# Original solution - this doesn't work!! 
# 
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    # Build Graph from edge list 
    graph = {} 
    for course, prereq in prerequisites:
        if course not in graph:
            graph[course] = []
        graph[course].append(prereq)

    # BFS over the graph 
    queue = deque([ list(graph.keys())[0] ])
    visited = set()
    while queue:
        curr = queue.popleft()
        if curr not in graph:
            continue 

        if curr in visited:     
            return False 
        visited.add(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)
'''