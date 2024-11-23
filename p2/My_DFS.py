def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path.append(start)
    
    # If the end node is found, return the path
    if start == end:
        return path

    # Recursively visit each neighbor
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, visited, path)
            if result:  # If the end node was found in the recursive call, return the path
                return result
    
    # If the end node is not found, remove the current node from the path and backtrack
    path.pop()
    return None

# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [4],
    3: [2],
    4: [5,6],
    5: [3,7],
    6: [],
    7: [6],
}

# Starting DFS from node 2 to reach node 8
start_node = 1
end_node = 7
path = dfs(graph, start=start_node, end=end_node)

if path:
    print(f"Path from {start_node} to {end_node}: {path}")
else:
    print(f"No path found from {start_node} to {end_node}.")
