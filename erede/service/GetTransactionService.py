from .TransactionService import TransactionService


class GetTransactionService(TransactionService):
    def __init__(self, store):
        super(GetTransactionService, self).__init__(store)

        self.tid = None
        self.reference = None
        self.refunds = False

    def get_uri(self):
        if self.reference is not None:
            return "{}?reference={}".format(super().get_uri(), self.reference)

        if self.tid is None:
            raise ValueError("You need to specify one: the tid or the reference")

        if self.refunds:
            return "{}/{}/refunds".format(super().get_uri(), self.tid)

        return "{}/{}".format(super().get_uri(), self.tid)

    def execute(self):
        self.send_request(TransactionService.GET)
