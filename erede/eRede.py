from .service import *


class eRede:
    USER_AGENT = "eRede/1.0 (SDK; Python)"

    def __init__(self, store):
        """

        :type store: `erede.Store.Store`
        """
        self.store = store

    def authorize(self, transaction):
        return self.create(transaction)

    def create(self, transaction):
        """Create a transaction

        :type transaction: `erede.Transaction.Transaction`
        :rtype: `erede.Transaction.Transaction`
        """
        create_transaction = CreateTransactionService(self.store, transaction)

        return create_transaction.execute()

    def cancel(self, transaction):
        """Cancel a Transaction

        :type transaction: `erede.Transaction.Transaction`
        :rtype: `erede.Transaction.Transaction`
        """

        cancel_transaction = CancelTransactionService(self.store, transaction)

        return cancel_transaction.execute()

    def capture(self, transaction):
        """Capture a Transaction

        :type transaction: `erede.Transaction.Transaction`
        :rtype: `erede.Transaction.Transaction`
        """

        capture_transaction = CaptureTransactionService(self.store, transaction)

        return capture_transaction.execute()

    def get_by_tid(self, tid):
        """Get a Transaction by its TID

        :type transaction: `erede.Transaction.Transaction`
        :rtype: `erede.Transaction.Transaction`
        """

        get_transaction = GetTransactionService(self.store)
        get_transaction.tid = tid

        return get_transaction.execute()

    def get_by_reference(self, reference):
        """Get a Transaction by its reference

        :type transaction: `erede.Transaction.Transaction`
        :rtype: `erede.Transaction.Transaction`
        """

        get_transaction = GetTransactionService(self.store)
        get_transaction.reference = reference

        return get_transaction.execute()

    def get_refunds(self, tid):
        """Get a Transaction refunds

        :type transaction: `erede.Transaction.Transaction`
        :rtype: `erede.Transaction.Transaction`
        """

        get_transaction = GetTransactionService(self.store)
        get_transaction.tid = tid
        get_transaction.refunds = True

        return get_transaction.execute()

    def zero(self, transaction):
        """Verify a card

        :type transaction: `erede.Transaction.Transaction`
        :rtype: `erede.Transaction.Transaction`
        """

        amount = transaction.amount
        capture = transaction.capture

        transaction.amount = 0
        transaction.capture = True

        transaction = self.create(transaction)

        transaction.amount = amount
        transaction.capture = capture

        return transaction
