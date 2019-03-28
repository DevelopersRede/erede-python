from .RedeSerializable import RedeSerializable


class Antifraud(RedeSerializable):
    def __init__(self):
        self.recommendation = None
        self.riskLevel = None
        self.score = None
        self.success = False

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Antifraud()

        for k, v in dict.items():
            setattr(instance, k, v)

        return instance
