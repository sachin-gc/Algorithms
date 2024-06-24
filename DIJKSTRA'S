import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # Distance from start to start is 0
    # Priority queue to hold tuples of (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If current_distance is greater than distances[current_node], skip the loop
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If found a shorter path to the neighbor, update the distance and push to priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
print(f"Shortest distances from node {start_node}:")
print(dijkstra(graph, start_node))
