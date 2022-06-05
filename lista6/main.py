import networkx as nx
from matplotlib import pyplot as plt


class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        self.neighbors_vertices = []

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                self.neighbors_vertices.append(neighbor)
                neighbor.neighbors.append(self.name)
                neighbor.neighbors_vertices.append(self)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    self.neighbors_vertices.append(neighbor)
                    neighbor.neighbors.append(self.name)
                    neighbor.neighbors_vertices.append(self)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False

    def __repr__(self):
        return str(self.neighbors)


class Graph:
    def __init__(self):
        self.vertices = {}
        self.vertices_list = []

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors
            self.vertices_list.append(vertex)

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors
                self.vertices_list.append(vertex)

    def add_edge(self, vertex_from, vertex_to):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            vertex_from.add_neighbor(vertex_to)
            self.vertices[vertex_from.name] = vertex_from.neighbors
            self.vertices[vertex_to.name] = vertex_to.neighbors

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def dfs_util(self, temp, v, visited):
        # Mark the current vertex as visited
        visited[v] = True
        # Store the vertex to list

        # Repeat for all vertices adjacent
        # to this vertex v
        vertex = self.vertices_list[v - 1]
        temp.append(vertex)
        for i in vertex.neighbors:
            if not visited[i]:
                # Update the list
                temp = self.dfs_util(temp, i, visited)
        return temp

    # method to add an undirected edge

    # Method to retrieve connected components
    # in an undirected graph
    def connected_components(self):
        visited = []
        cc = []
        names = []
        for i in range(len(self.vertices_list) + 1):
            visited.append(False)
        for v in self.vertices_list:
            if not visited[v.name]:
                temp = []
                _vertices = self.dfs_util(temp, v.name, visited)
                cc.append(_vertices)
                names.append([vertex.name for vertex in _vertices])
        return names, cc

    @property
    def adjacency_list(self):
        if len(self.vertices) >= 1:
            return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()

    @property
    def adjacency_matrix(self):
        if len(self.vertices) >= 1:
            vertex_names = sorted(self.vertices.keys())
            vertex_indices = dict(zip(vertex_names, range(len(vertex_names))))
            import numpy as np
            adjacency_matrix = np.zeros(shape=(len(self.vertices), len(self.vertices)))
            for i in range(len(vertex_names)):
                for j in range(i, len(self.vertices)):
                    for el in self.vertices[vertex_names[i]]:
                        j = vertex_indices[el]
                        adjacency_matrix[i, j] = 1
            return adjacency_matrix
        else:
            return dict()

    def min_distance(self, dist, spt_set):

        # Initialize minimum distance for next node
        _min = float('inf')

        # Search not the nearest vertex not in the
        # shortest path tree
        min_index = -1
        for v in range(len(self.vertices_list)):
            if dist[v] < _min and not spt_set[v]:
                _min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src, dst=1):
        src = src - 1
        dist = [float('inf')] * len(self.vertices_list)
        dist[src] = 0
        spt_set = [False] * len(self.vertices_list)

        for _ in range(len(self.vertices_list)):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.min_distance(dist, spt_set)

            # Put the minimum distance vertex in the
            # shortest path tree
            spt_set[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(len(self.vertices_list)):
                if (self.adjacency_matrix[u][v] > 0 and
                        not spt_set[v] and
                        dist[v] > dist[u] + self.adjacency_matrix[u][v]):
                    dist[v] = dist[u] + self.adjacency_matrix[u][v]

        print(f'najkrótsza odległość od {src + 1} do {dst} to:'
              f'{dist[dst - 1]}')
        print(f'Lista dystansów do poszczególnych wierzchołków:')
        for node in range(len(self.vertices_list)):
            print(node + 1, "\t\t", dist[node])


def graph(__g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(__g.adjacency_list) + '\n' + '\n' + str(__g.adjacency_matrix)


def random_graph(nodes):
    import random
    vertices = [Vertex(i) for i in range(1, nodes + 1)]
    for vertex in vertices:
        neighbor = random.choice(vertices)
        if neighbor == vertex:
            continue
        vertex.add_neighbor(neighbor)
    g = Graph()
    g.add_vertices(vertices)
    return g


def graph_to_nx(_graph):
    nx_graph = nx.Graph()
    for vertex in _graph.vertices_list:
        if not vertex.neighbors_vertices:
            nx_graph.add_node(vertex.name)
        for conn in vertex.neighbors_vertices:
            nx_graph.add_edge(vertex.name, conn.name)

    return nx_graph


def plot_graph(_graph):
    _g = graph_to_nx(_graph)
    nx.draw_networkx(_g)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("on")
    plt.tight_layout()
    plt.show()


###################################################################################
if __name__ == '__main__':
    _graph = random_graph(9)
    print(graph(_graph))
    _cc, connected_graphs = _graph.connected_components()
    print("Following are connected components")
    print(_cc)
    graphs = []
    for __vertices in connected_graphs:
        __graph = Graph()
        __graph.add_vertices(__vertices)
        graphs.append(__graph)
    _graph.dijkstra(9)
    plot_graph(_graph)
    for __graph in graphs:
        plot_graph(__graph)
