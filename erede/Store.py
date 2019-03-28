from .Environment import Environment


class Store:
    def __init__(self, filliation, token, environment=None):
        """

        :type filliation: `string`
        :type token: `string`
        :type environment: `erede.Environment.Environment`
        """
        if environment is None:
            environment = Environment.production()

        self.filliation = filliation
        self.token = token
        self.environment = environment
