class Maze:
    def __init__(self, graph):
        self.graph = graph  # The maze represented as an adjacency list

    def dfs(self, start, target):
        visited = set()  # To keep track of visited nodes
        return self._dfs_recursive(start, target, visited)

    def _dfs_recursive(self, node, target, visited):
        if node not in visited:
            print(f"Visiting node: {node}")
            visited.add(node)

            if node == target:
                return True

            for neighbor in self.graph.get(node, []):
                if self._dfs_recursive(neighbor, target, visited):
                    return True

        return False


# Example usage:
# Create a graph where each node has a list of its neighbors
maze_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G', 'H'],
    'F': [],
    'G': [],
    'H': []
}

maze = Maze(maze_graph)
start_node = 'A'
target_node = 'G'  # The cheese is at node 'G'

found = maze.dfs(start_node, target_node)
print("Cheese found!" if found else "Cheese not found.")
