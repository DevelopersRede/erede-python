from .RedeSerializable import RedeSerializable


class Document(RedeSerializable):
    def __init__(self, document_type, number):
        self.type = document_type
        self.number = number
