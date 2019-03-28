import requests
import erede

from erede.Transaction import Transaction
from erede.RedeError import RedeError


class TransactionService:
    GET = "get"
    POST = "post"
    PUT = "put"

    def __init__(self, store):
        """

        :type store: `erede.Store.Store`
        """
        self.store = store

    def execute(self):
        raise NotImplementedError("Not implemented")

    def get_uri(self):
        return "{}/transactions".format(self.store.environment.endpoint)

    def send_request(self, method, body=None):
        headers = {'User-Agent': "{} Store/{}".format(erede.eRede.USER_AGENT, self.store.filliation),
                   "Accept": "application/json",
                   "Content-Type": "application/json"}

        response = getattr(requests, method)(self.get_uri(),
                                             auth=(self.store.filliation, self.store.token),
                                             data=body,
                                             headers=headers)
        '''
        :type response: `requests.Response`
        '''

        if response.status_code >= 400:
            error = response.json()

            raise RedeError(error.get("returnMessage", "opz"), error.get("returnCode", 0))

        return Transaction.unserialize(response.json())
