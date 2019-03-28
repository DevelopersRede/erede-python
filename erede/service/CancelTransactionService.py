from .TransactionService import TransactionService


class CancelTransactionService(TransactionService):
    def __init__(self, store, transaction):
        """

        :type store: `erede.Store.Store`
        :type transaction: `erede.Transaction.Transaction`
        """
        super(CancelTransactionService, self).__init__(store)

        self.transaction = transaction

    def get_uri(self):
        return "{}/{}/refunds".format(super().get_uri(), self.transaction.tid)

    def execute(self):
        self.send_request(TransactionService.POST, self.transaction.to_json())
