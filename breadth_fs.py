from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            print(f"Visiting: {node}")
            visited.add(node)

            if node == goal:
                return path
            
            for neighbour in graph[node]:
                queue.append((neighbour, path + [neighbour]))

graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': ['F'],
'F': []
}

result = bfs(graph, 'A', 'F')
print("Shortest path to goal: ", result)