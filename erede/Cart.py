from .Address import Address
from .Consumer import Consumer
from .Iata import Iata
from .RedeSerializable import RedeSerializable


class Cart(RedeSerializable):
    def __init__(self):
        self.billing = None
        self.consumer = None
        self.environment = None
        self.iata = None
        self.items = None
        self.shipping = None

    def adress(self, address_type=None):
        """

        :type address_type: `int`
        """
        if address_type is None:
            address_type = Address.BOTH

        address = Address()

        if (address_type & Address.BILLING) == Address.BILLING:
            self.billing = address

        if (address_type & Address.SHIPPING) == Address.SHIPPING:
            self.shipping = [address]

        return address

    def add_item(self, item):
        """

        :type item: `erede.Item.Item`
        """
        if self.items is None:
            self.items = []

        self.items.append(item)

        return self

    def consumer(self, name, email, cpf):
        """

        :type name: `string`
        :type email: `string`
        :type cpf: `string`
        :rtype: `erede.Consumer.Consumer`
        """
        self.consumer = Consumer(name, email, cpf)

        return self.consumer

    def set_iata(self, flight):
        """

        :type flight: `erede.Flight.Flight`
        """
        self.iata = Iata()
        self.iata.add_flight(flight)

        return self
