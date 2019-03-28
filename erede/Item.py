from .RedeSerializable import RedeSerializable


class Item(RedeSerializable):
    PHYSICAL = 1
    DIGITAL = 2
    SERVICE = 3
    AIRLINE = 4

    def __init__(self, item_id, quantity, item_type=None):
        if item_type is None:
            item_type = Item.PHYSICAL

        self.id = item_id
        self.quantity = quantity
        self.type = item_type
        self.amount = None
        self.description = None
        self.discount = None
        self.freight = None
        self.shippingType = None
