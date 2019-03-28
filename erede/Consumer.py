from .Document import Document
from .Phone import Phone
from .RedeSerializable import RedeSerializable


class Consumer(RedeSerializable):
    MALE = "M"
    FEMALE = "F"

    def __init__(self, name, email, cpf):
        """

        :type name: `string`
        :type email: `string`
        :type cpf: `string`
        """
        self.cpf = cpf
        self.email = email
        self.name = name
        self.documents = None
        self.gender = None
        self.phone = None

    def add_document(self, document_type, number):
        """

        :type document_type: `string`
        :type number: `string`
        :rtype: `erede.Document.Document`
        """
        if self.documents is None:
            self.documents = []

        document = Document(document_type, number)

        self.documents.append(document)

        return document

    def add_phone(self, ddd, number, phone_type=None):
        if phone_type is None:
            phone_type = Phone.CELLPHONE

        phone = Phone(ddd, number, phone_type)

        self.phone = phone

        return phone
