class Refund:
    def __init__(self):
        self.amount = None
        self.refundDateTime = None
        self.refundId = None
        self.status = None

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Refund()

        for k, v in dict.items():
            setattr(instance, k, v)

        return instance
