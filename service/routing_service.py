from model.minheap import MinHeap


class RoutingService:

    def __init__(self, graph, origin):
        """
        Uses Dijkstra's algorithm to find the best delivery route
        for a given starting location represented as a vertex on
        the graph.
        :param graph: used to compare to routes.
        :param origin: the starting location
        """
        self.graph = graph
        self.origin = origin
        self._dijkstra()

    def shortest_route(self, destination):
        """
        Retrieves a list of vertices that represent the
        shortest path to the given destination vertex.
        :param destination: vertex in which to get the shortest path to.
        :return: shortest path to the destination.
        """
        route = [destination]
        current = destination
        while current is not self.origin:
            route.append(current.previous)
            current = current.previous
        route.reverse()
        return route

    def _dijkstra(self):
        self.origin.distance = 0
        unvisited_queue = MinHeap()
        for vertex in self.graph:
            unvisited_queue.push((vertex.distance, vertex))
        while unvisited_queue:
            smallest_vertex = unvisited_queue.pop()
            current_vertex = smallest_vertex[1]
            current_vertex.visited = True
            for adjacent_vertex in current_vertex.adjacent():
                if adjacent_vertex.visited:
                    continue
                new_distance = current_vertex.distance + current_vertex.weight(adjacent_vertex)
                if new_distance < adjacent_vertex.distance:
                    adjacent_vertex.distance = new_distance
                    adjacent_vertex.previous = current_vertex
                    unvisited_queue.push((adjacent_vertex.distance, adjacent_vertex))
