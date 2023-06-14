from sys import maxsize

INF = int(0x3f3f3f3f)

# Class to represent an edge in the graph
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

# Class to represent a graph
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.edge = []

    # Add an edge to the graph
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        e = Edge(u, v, w)
        self.edge.append(e)

    # Remove an edge from the graph
    def remove_edge(self, u, v, w):
        self.adj[u].remove((v, w))
        self.adj[v].remove((u, w))

    # Find the shortest path between two vertices using Dijkstra's algorithm
    def shortest_path(self, u, v):
        ds = set()
        dist = [INF] * self.V
        ds.add((0, u))
        dist[u] = 0

        while ds:
            tmp = ds.pop()
            s = tmp[1]
            for i in self.adj[s]:
                t = i[0]
                weight = i[1]
                if dist[t] > dist[s] + weight:
                    if dist[t] != INF:
                        if (dist[t], t) in ds:
                            ds.remove((dist[t], t))
                    dist[t] = dist[s] + weight
                    ds.add((dist[t], t))
        return dist[v]

    # Find the minimum cycle in the graph
    def find_minimum_cycle(self) -> int:
        min_cycle = maxsize
        E = len(self.edge)
        for i in range(E):
            e = self.edge[i]
            self.remove_edge(e.u, e.v, e.weight)
            distance = self.shortest_path(e.u, e.v)
            min_cycle = min(min_cycle, distance + e.weight)
            self.add_edge(e.u, e.v, e.weight)

        return min_cycle


if __name__ == "__main__":
    V = 301
    g = Graph(V)
    edge = []
    N = int(input())
    for i in range(N):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    print(g.find_minimum_cycle())
