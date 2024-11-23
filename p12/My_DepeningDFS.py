# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['F', 'G'],
    'D': ['H','I'],
    'E': ['B'],
    
    'F': ['K', 'C'],
    'G': ['C'],
    'H': ['D'],
    'I': ['D'],
    'K': ['F']
}

def dfs_limited(node, target, depth, visited):
    """
    Perform depth-limited DFS from the current node.
    """
    if depth == 0:
        if node == target:
            return [node]
        else:
            return None
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            path = dfs_limited(neighbor, target, depth - 1, visited)
            if path:
                return [node] + path
    visited.remove(node)
    return None

def iterative_deepening_search(start, target, max_depth):
    """
    Perform IDS to find a path from start to target up to max_depth.
    """
    for depth in range(max_depth + 1):
        visited = set()
        print(f"Searching at depth {depth}...")
        path = dfs_limited(start, target, depth, visited)
        if path:
            return path
    return None

# Example usage
start_node = 'A'
target_node = 'G'
max_depth = 3

path = iterative_deepening_search(start_node, target_node, max_depth)

if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found.")

