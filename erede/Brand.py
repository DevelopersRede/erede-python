from .RedeSerializable import RedeSerializable


class Brand(RedeSerializable):
    def __init__(self):
        self.name = None
        self.responseCode = None
        self.responseMessage = None

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Brand()

        for k, v in dict.items():
            setattr(instance, k, v)

        return instance
