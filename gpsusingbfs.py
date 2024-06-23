from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node]) # Initializing the queue
    reachable_nodes = []

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            reachable_nodes.append(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return reachable_nodes

# Example usage:
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    source_node = 'A'
    reachable_nodes = bfs(graph, source_node)
    print(f"Reachable nodes from {source_node}: {reachable_nodes}")
