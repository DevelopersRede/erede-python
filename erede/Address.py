from .RedeSerializable import RedeSerializable


class Address(RedeSerializable):
    BILLING = 1
    SHIPPING = 2
    BOTH = 3
    APARTMENT = 1
    HOUSE = 2
    COMMERCIAL = 3
    OTHER = 4

    def __init__(self):
        self.address = None
        self.addresseeName = None
        self.city = None
        self.number = None
        self.state = None
        self.type = None
        self.zipCode = None

