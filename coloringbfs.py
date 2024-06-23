from collections import deque, defaultdict


def is_bipartite(graph, start):
    # Dictionary to store the color of each node
    color = {}
    # Queue for BFS
    queue = deque([start])
    # Start coloring the start node with red (1)
    color[start] = 1

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in color:
                # Color the neighbor with the opposite color
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                # If the neighbor has the same color, the graph is not bipartite
                return False

    # If we successfully colored the graph with 2 colors, it's bipartite
    return True


# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [1, 3,4,5],
    3: [1, 2,6,7],
    4: [2, 5,9,8],
    5:[2,4,9],
    6:[3,7],
    7:[6,3],
    8:[4,9],
    9:[4,5,8,10],
    10:[9],

}

start_node = 1
if is_bipartite(graph, start_node):
    print("The graph is bipartite.")
else:
    print("The graph is not bipartite.")
