class Graph:
    INF = float('inf')

    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print_mst(self, parent):
        print("Edge     Weight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}       {self.graph[i][parent[i]]}")

    def min_key(self, key, mst_set):
        min_index = -1
        _min = self.INF
        for v in range(self.V):
            if key[v] < _min and not mst_set[v]:
                _min = key[v]
                min_index = v
        return min_index

    def prims(self):
        key = [self.INF for _ in range(self.V)]
        parent = [0 for _ in range(self.V)]
        key[0] = 0
        mst_set = [False for _ in range(self.V)]
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if key[v] > self.graph[u][v] > 0 and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.prims()
