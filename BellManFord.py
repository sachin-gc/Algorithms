class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        # Step 1: Initialize distances from source to all other vertices as INFINITE
        distance = [float('inf')] * self.vertices
        distance[source] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        # Step 3: Check for negative-weight cycles
        for u, v, weight in self.edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                print("Graph contains negative weight cycle")
                return

        # Print the calculated shortest distances
        self.print_solution(distance)

    def print_solution(self, distance):
        print("Vertex Distance from Source")
        for i in range(self.vertices):
            print(f"{i}\t\t{distance[i]}")

def main():
    # Create a graph given in the above diagram
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
    g = Graph(vertices)

    print("Enter the edges in the format (u v weight):")
    for _ in range(edges):
        u, v, weight = map(int, input().split())
        g.add_edge(u, v, weight)

    source = int(input("Enter the source vertex: "))

    # Measure execution time
    import time
    start_time = time.time()
    
    g.bellman_ford(source)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

if __name__ == "__main__":
    main()