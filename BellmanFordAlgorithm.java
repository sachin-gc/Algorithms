import java.util.*;

// Class to represent a graph edge
class Edge {
    int source, destination, weight;

    Edge(int source, int destination, int weight) {
        this.source = source;
        this.destination = destination;
        this.weight = weight;
    }
}

// Class to represent a graph
class Graph {
    int V, E; // V -> Number of vertices, E -> Number of edges
    Edge[] edges;

    // Creates a graph with V vertices and E edges
    Graph(int V, int E) {
        this.V = V;
        this.E = E;
        edges = new Edge[E];
    }

    // Function to find the shortest paths from source using Bellman-Ford algorithm
    void bellmanFord(int source) {
        int[] distance = new int[V];

        // Step 1: Initialize distances from source to all other vertices as INFINITE
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[source] = 0;

        // Step 2: Relax all edges |V| - 1 times
        for (int i = 1; i < V; ++i)// this for loop is for ralaxation of n-1 times         
        {
            for (int j = 0; j < E; ++j) {
                int u = edges[j].source;
                int v = edges[j].destination;
                int weight = edges[j].weight;
                if (/*distance[u] != Integer.MAX_VALUE && 8*/distance[u] + weight < distance[v])
                    distance[v] = distance[u] + weight;
            }
        }

        // Step 3: Check for negative-weight cycles
        // If we can still update the distance[], then there is a negative cycle
        for (int i = 0; i < E; ++i) {
            int u = edges[i].source;
            int v = edges[i].destination;
            int weight = edges[i].weight;
            if (/*distance[u] != Integer.MAX_VALUE &&*/ distance[u] + weight < distance[v]) {
                System.out.println("Graph contains negative weight cycle");
                return;
            }
        }

        // Print the distance array
        printDistances(distance);
    }

    // A utility function to print the constructed distance array
    void printDistances(int[] distance) {
        System.out.println("Vertex   Distance from Source");
        for (int i = 0; i < V; ++i)
            System.out.println(i + "\t\t" + distance[i]);
    }
}

// Main class
public class BellmanFordAlgorithm {
    public static void main(String[] args) {
        // Create a graph
        int V = 6; // Number of vertices in graph
        int E = 9; // Number of edges in graph
        Graph graph = new Graph(V, E);

        // Add edge 0-1 (source, destination, weight)
        graph.edges[0] = new Edge(0, 1, 6);

        // Add edge 0-2
        graph.edges[1] = new Edge(0, 2, 4);

        // Add edge 1-2
        graph.edges[2] = new Edge(0, 3, 5);

        // Add edge 1-3
        graph.edges[3] = new Edge(1, 4, -1);

        // Add edge 1-4
        graph.edges[4] = new Edge(2, 4, 3);

        // Add edge 3-2
        graph.edges[5] = new Edge(3, 2, -2);

        // Add edge 3-1
        graph.edges[6] = new Edge(3, 5, -1);

        // Add edge 4-3
        graph.edges[7] = new Edge(4, 5, 3);
        graph.edges[8] = new Edge(2, 1, -2);

        int source = 0; // Source vertex

        // Apply Bellman-Ford algorithm from the given source
        graph.bellmanFord(source);
}
}
