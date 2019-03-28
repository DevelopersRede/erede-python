class RedeError(Exception):
    def __init__(self, message, code):
        super(RedeError, self).__init__(message)

        self.code = code
