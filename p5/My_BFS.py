from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print BFS of graph and return the path from start to end node
    def BFS(self, start, end):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        # Create a queue for BFS
        queue = []
        # To track the path
        parent = [-1] * (max(self.graph) + 1)

        # Mark the source node as visited and enqueue it
        queue.append(start)
        visited[start] = True

        while queue:
            # Dequeue a vertex from queue
            current_node = queue.pop(0)

            # If the end node is found, return the path
            if current_node == end:
                path = []
                while current_node != -1:
                    path.append(current_node)
                    current_node = parent[current_node]
                return path[::-1]  # Return the path in reverse order

            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent node has not been visited, mark it visited and enqueue it
            for neighbor in self.graph[current_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current_node

        # If no path is found
        return None

# Driver code
if __name__ == '__main__':
    # Create a graph
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(3, 6)
    g.addEdge(4,2)
     
    g.addEdge(5, 8)
    g.addEdge(5, 7)
    
    g.addEdge(6, 8)
    g.addEdge(7,8)
   
   

    # Define start and end node
    start_node = 1
    end_node = 8

    print(f"Following is the path from node {start_node} to node {end_node}:")
    path = g.BFS(start_node, end_node)

    if path:
        print(" -> ".join(map(str, path)))
    else:
        print(f"No path found from node {start_node} to node {end_node}.")
