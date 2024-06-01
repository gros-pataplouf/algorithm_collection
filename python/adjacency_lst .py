adjacency_lst = {
  'a': ['b', 'c', 'd'],
  'b': ['a', 'd'],
  'c': ['a'],
  'd': ['a', 'b', 'e'],
  'e': ['d']
}

# When we initialize our graph, we will allow the user to pass a boolean value to indicate if it is undirected.
#This value will default to true.
# We will implement methods to create vertexes, add edges to connect them, and remove a vertex.
#The implementation will take the following shape:
#We will assume the data contained in vertexes (nodes) is unique, and this value will represent the key in the adjacency list as well.

class Graph:
    def __init__(self, undirected = True):
        self.adjacency_list = {}
        self.undirected = undirected

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        self.adjacency_list[source].push(destination)
        if not self.undirected:
            self.adjacency_list[destination].push(source)

    def remove_vertex(self, vertex):
        # Remove a vertex and clean up the edges pointing to it
        connected_vertices = self.adjacency_list[vertex]
        self.adjacency_list.pop(vertex)
        for conn_vert in connected_vertices:
            if vertex in self.adjacency_list[conn_vert]:
                self.adjacency_list.remove(vertex)
    def remove_vertex_alternative(self, vertex):
        self.adjacency_list.pop(vertex)

        for node in self.adjacency_list.keys():
            self.adjacency_list[node] = [v for v in self.adjacency_list[node] if v != vertex]

