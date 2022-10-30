'''
Given an (unweighted) graph, return the length of the shortest path between two nodes A and B, in terms of the number of edges.

Input:

graph: {
  0: [1, 2],
  1: [0, 2, 3],
  2: [0, 1],
  3: [1]
}
A: 0
B: 3
Output: 2
'''

from collections import deque

def shortest_path(graph, a, b):
    def get_neighbors(node):
        return graph[node]

    # BFS template
    def bfs(root, target):
        queue = deque([root])
        visited = set([root])
        level = 0
        while len(queue) > 0:
            n = len(queue)
            for n in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            level += 1

    return bfs(a, b)

#Testing Code
graph: {
  0: [1, 2],
  1: [0, 2, 3],
  2: [0, 1],
  3: [1]
}

print(shortest_path(0, 3))