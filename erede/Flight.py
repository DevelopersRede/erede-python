from .RedeSerializable import RedeSerializable


class Flight(RedeSerializable):
    def __init__(self, number, flight_from, to, date):
        self.number = number
        self.From = flight_from
        self.to = to
        self.date = date
        self.passenger = None

    def add_passenger(self, passenger):
        if self.passenger is None:
            self.passenger = []

        self.passenger.append(passenger)

        return self
