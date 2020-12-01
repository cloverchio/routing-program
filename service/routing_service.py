from model.graph import Vertex, Graph


class RoutingService:

    def __init__(self, graph, origin):
        """
        Uses Dijkstra's algorithm to find the best delivery route
        for a given starting location represented as a vertex on
        the graph.
        :param graph: used to compare to routes.
        :param origin: the starting location
        """
        origin.distance = 0
        unvisited_queue = [(vertex.distance, vertex) for vertex in graph]
        while unvisited_queue:
            unvisited_queue.sort(key=lambda pair: pair[0], reverse=True)
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

        # TODO finish implementation
