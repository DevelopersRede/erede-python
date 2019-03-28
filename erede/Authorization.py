class Authorization:
    def __init__(self):
        self.affiliation = None
        self.amount = None
        self.authorizationCode = None
        self.cardBin = None
        self.cardHolderName = None
        self.dateTime = None
        self.installments = None
        self.kind = None
        self.last4 = None
        self.nsu = None
        self.origin = None
        self.reference = None
        self.returnCode = None
        self.returnMessage = None
        self.status = None
        self.subscription = None
        self.tid = None

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Authorization()

        for k, v in dict.items():
            setattr(instance, k, v)

        return instance
