from .RedeSerializable import RedeSerializable


class Additional(RedeSerializable):
    def __init__(self, gateway=None, module=None):
        self.gateway = gateway
        self.module = module

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Additional()

        for k, v in dict.items():
            setattr(instance, k, v)

        return instance
