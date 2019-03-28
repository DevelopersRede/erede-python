from .TransactionService import TransactionService


class CreateTransactionService(TransactionService):
    def __init__(self, store, transaction):
        """

        :type store: `erede.Store.Store`
        :type transaction: `erede.Transaction.Transaction`
        """
        super(CreateTransactionService, self).__init__(store)

        self.transaction = transaction

    def execute(self):
        return self.send_request(TransactionService.POST, self.transaction.to_json())

