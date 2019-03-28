from .RedeSerializable import RedeSerializable


class Environment(RedeSerializable):
    PRODUCTION = "https://api.userede.com.br/erede"
    SANDBOX = "https://api.userede.com.br/desenvolvedores"
    VERSION = "v1"

    def __init__(self, base_url, version=None):
        if version is None:
            version = Environment.VERSION

        self.ip = None
        self.sessionId = None
        self.endpoint = "{}/{}".format(base_url, version)

    @staticmethod
    def production():
        """

        :rtype: `erede.Environment.Environment`
        """
        return Environment(Environment.PRODUCTION)

    @staticmethod
    def sandbox():
        """

        :rtype: `erede.Environment.Environment`
        """
        return Environment(Environment.SANDBOX)
