from .Phone import Phone
from .RedeSerializable import RedeSerializable


class Passenger(RedeSerializable):
    def __init__(self, name, email, ticket):
        self.name = name
        self.email = email
        self.ticket = ticket
        self.phone = None

    def set_phone(self, ddd, number, phone_type=None):
        if phone_type is None:
            phone_type = Phone.CELLPHONE

        self.phone = Phone(ddd, number, phone_type)
