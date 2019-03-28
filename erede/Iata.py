from .RedeSerializable import RedeSerializable


class Iata(RedeSerializable):
    def __init__(self, code, departure_tax):
        self.code = code
        self.departureTax = departure_tax
        self.flight = None

    def add_flight(self, flight):
        if self.flight is None:
            self.flight = []

        self.flight.append(flight)

        return self
