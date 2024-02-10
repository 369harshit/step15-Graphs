from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def dfs(self, vertex, visited):
        visited[vertex] = True
        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def count_provinces(self):
        visited = [False] * self.vertices
        province_count = 0

        for vertex in range(self.vertices):
            if not visited[vertex]:
                province_count += 1
                self.dfs(vertex, visited)

        return province_count

# Example Usage
if __name__ == "__main__":
    # Initialize the graph
    vertices = 5
    g = Graph(vertices)

    # Add edges
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 4)

    # Find the number of provinces
    provinces = g.count_provinces()

    print("Number of provinces:", provinces)
