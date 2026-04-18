#DFS using Stack
def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()

        if node not in visited:
            print(f"Visiting: {node}")
            visited.add(node)

            if node == goal:
                return path
            
            for neighbour in reversed(graph[node]):
                stack.append((neighbour, path + [neighbour]))

graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': ['F'],
'F': []
}

result = dfs(graph, 'A', 'F')
print("Path to goal: ", result)