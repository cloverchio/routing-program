class Vertex:

    def __init__(self, key):
        self._key = key
        self._adjacent = {}
        self._distance = float('inf')
        self._visited = False
        self._previous = None

    def add_adjacent(self, vertex, weight=0):
        self._adjacent[vertex] = weight

    def adjacent(self):
        return self._adjacent.keys()

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance):
        self._distance = distance

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, visited):
        self._visited = visited

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, previous):
        self._previous = previous

    def __str__(self):
        return str(self._key) + ': ' + str([(vertex.key, weight) for vertex, weight in self._adjacent.items()])


class Graph:

    def __init__(self):
        self.vertices = {}
        self.vertex_count = 0

    def __len__(self):
        return self.vertex_count

    def __contains__(self, item):
        return self.vertices[item] is not None

    def get_vertex(self, key):
        """
        Retrieves the vertex associated with the given key.
        :param key: in which to retrieve the vertex for.
        :return: vertex associated with the key or None if not found.
        """
        if key in self.vertices:
            return self.vertices[key]
        return None

    def get_vertices(self):
        """
        Retrieves all vertices within the graph.
        :return: list of vertices.
        """
        return [str(vertex) for vertex in self.vertices.values()]

    def add_vertex(self, key):
        """
        Adds a new vertex to the graph for the given key.
        :param key: in which to label the vertex.
        :return:
        """
        self.vertex_count += 1
        self.vertices[key] = Vertex(key)

    def remove_vertex(self, key):
        """
        Removes the vertex associated with the given key.
        :param key: in which to remove the vertex for.
        :return:
        """
        self.vertices.pop(key)

    def add_edge(self, origin, destination, weight=0):
        """
        Creates an edge mapping between the given vertices.
        Origin and destination vertices must already be present in the graph.
        :param origin: vertex in which the edge should originate from.
        :param destination: vertex in which the edge should direct to.
        :param weight: weight to be associated with the given edge.
        :return:
        """
        if origin not in self.vertices:
            raise TypeError("origin vertex not found")
        if destination not in self.vertices:
            raise TypeError("destination vertex not found")
        self.vertices[origin].add_adjacent(self.vertices[destination], weight)
        self.vertices[destination].add_adjacent(self.vertices[origin], weight)
