from .RedeSerializable import RedeSerializable


class SubMerchant(RedeSerializable):
    def __init__(self, mcc, city, country):
        self.mcc = mcc
        self.city = city
        self.country = country
