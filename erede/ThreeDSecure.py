from .RedeSerializable import RedeSerializable


class ThreeDSecure(RedeSerializable):
    CONTINUE_ON_FAILURE = "continue"
    DECLINE_ON_FAILURE = "decline"

    def __init__(self):
        self.cavv = None
        self.eci = None
        self.embedded = True
        self.onFailure = None
        self.url = None
        self.userAgent = eRede.USER_AGENT
        self.xid = None
        self.threeDIndicator = "1"
        self.directoryServerTransactionId = None

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Additional()

        for k, v in dict.items():
            setattr(instance, k, v)

        return instance
