from .Additional import Additional
from .Antifraud import Antifraud
from .Authorization import Authorization
from .Cart import Cart
from .Environment import Environment
from .RedeSerializable import RedeSerializable
from .ThreeDSecure import ThreeDSecure
from .Url import Url
from .Refund import Refund
from .Capture import Capture
from .Iata import Iata


class Transaction(RedeSerializable):
    CREDIT = "credit"
    DEBIT = "debit"

    ORIGIN_EREDE = 1
    ORIGIN_VISA_CHECKOUT = 4
    ORIGIN_MASTERPASS = 6

    def __init__(self, amount, reference):
        """

        :type amount: `int`
        :type reference: `string`
        """

        """
        
        """
        self.amount = round(amount*100)
        self.reference = reference
        self.additional = None
        self.antifraud = None
        self.antifraudRequired = None
        self.authorization = None
        self.authorizationCode = None
        self.cancelId = None
        self.capture = None
        self.cardBin = None
        self.cardHolderName = None
        self.cardNumber = None
        self.cart = None
        self.dateTime = None
        self.distributorAffiliation = None
        self.expirationMonth = None
        self.expirationYear = None
        self.iata = None
        self.installments = None
        self.kind = None
        self.last4 = None
        self.nsu = None
        self.origin = None
        self.refundDateTime = None
        self.refundId = None
        self.refunds = None
        self.requestDateTime = None
        self.returnCode = None
        self.returnMessage = None
        self.securityCode = None
        self.softDescriptor = None
        self.storageCard = None
        self.subscription = None
        self.threeDSecure = None
        self.tid = None
        self.urls = None
        self.subMerchant = None
        self.paymentFacilitatorID = None

    def add_url(self, url, kind=None):
        if kind is None:
            kind = Url.CALLBACK

        if self.urls is None:
            self.urls = []

        self.urls.append(Url(url, kind))

        return self

    def set_antifraud(self, environment=None):
        if environment is None:
            environment = Environment.production()

        cart = Cart()
        cart.environment = environment

        self.antifraudRequired = True
        self.cart = cart

        return cart

    def credit_card(self, card_number, security_code, expiration_month, expitarion_year, card_holder_name):
        return self.card(card_number, security_code, expiration_month, expitarion_year, card_holder_name,
                         Transaction.CREDIT)

    def debit_card(self, card_number, security_code, expiration_month, expitarion_year, card_holder_name):
        return self.card(card_number, security_code, expiration_month, expitarion_year, card_holder_name,
                         Transaction.DEBIT)

    def card(self, card_number, security_code, expiration_month, expitarion_year, card_holder_name, kind):
        self.cardNumber = card_number
        self.securityCode = security_code
        self.expirationMonth = expiration_month
        self.expirationYear = expitarion_year
        self.cardHolderName = card_holder_name
        self.kind = kind

        return self

    def capture_transaction(self, capture=True):
        if not capture and self.kind == Transaction.DEBIT:
            raise ValueError("Debit transactions will always be captured")

        self.capture = capture

        return self

    def mcc(self, soft_descriptor, payment_facilitator_id, sub_merchant):
        self.softDescriptor = soft_descriptor
        self.paymentFacilitatorID = payment_facilitator_id
        self.subMerchant = sub_merchant

        return self

    def three_d_secure(self, on_failure=ThreeDSecure.DECLINE_ON_FAILURE, embed=True, transaction_id="", indicator="1"):
        three_d_secure = ThreeDSecure()
        three_d_secure.onFailure = on_failure
        three_d_secure.embedded = embed
        three_d_secure.directoryServerTransactionId = transaction_id
        three_d_secure.threeDIndicator = indicator

        self.threeDSecure = three_d_secure

        return self

    def set_additional(self, gateway=None, module=None):
        """

        :type gateway: `int`
        :type module: `int`
        :rtype: `erede.Transaction.Transaction`
        """
        self.additional = Additional(gateway, module)

        return self

    def set_iata(self, code, departure_tax):
        self.iata = Iata(code, departure_tax)

        return self

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Transaction(dict.get("amount", 0), dict.get("reference", ""))

        for k, v in dict.items():
            if k == "refunds":
                instance.refunds = []

                for r in dict.get("refunds", []):
                    instance.refunds.append(Refund.unserialize(r))

                continue

            if k == "urls":
                instance.urls = []

                for u in dict.get("urls", []):
                    instance.urls.append(Url.unserialize(u))

                continue

            if k == "capture":
                instance.capture = Capture.unserialize(v)

                continue

            if k == "authorization":
                instance.authorization = Authorization.unserialize(v)

                continue

            if k == "threeDSecure":
                instance.threeDSecure = ThreeDSecure.unserialize(v)

                continue

            if k == "antifraud":
                instance.antifraud = Antifraud.unserialize(v)

                continue

            if k == "additional":
                instance.additional = Additional.unserialize(v)

                continue

            setattr(instance, k, v)

        return instance
