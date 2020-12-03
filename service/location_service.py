from model.graph import Graph

class LocationService:

    def __init__(self, routing_service, location_data):
        self.routing_service = routing_service
        self.location_data = location_data

    # TODO finish implementing