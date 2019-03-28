from .RedeSerializable import RedeSerializable


class Phone(RedeSerializable):
    CELLPHONE = 1
    HOME = 2
    WORK = 3
    OTHER = 4

    def __init__(self, ddd, number, phone_type=None):
        if phone_type is None:
            phone_type = Phone.CELLPHONE

        self.ddd = ddd
        self.number = number
        self.type = phone_type
