class Capture:
    def __init__(self):
        self.amount = None
        self.dateTime = None
        self.nsu = None

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Capture()

        for k, v in dict.items():
            setattr(instance, k, v)

        return instance
