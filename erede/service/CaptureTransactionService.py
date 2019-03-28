from .TransactionService import TransactionService


class CaptureTransactionService(TransactionService):
    def __init__(self, store, transaction):
        """

        :type store: `erede.Store.Store`
        :type transaction: `erede.Transaction.Transaction`
        """
        super(CaptureTransactionService, self).__init__(store)

        self.transaction = transaction

    def get_uri(self):
        return "{}/{}".format(super().get_uri(), self.transaction.tid)

    def execute(self):
        self.send_request(TransactionService.PUT, self.transaction.to_json())
