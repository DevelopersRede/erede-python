from .RedeSerializable import RedeSerializable


class Url(RedeSerializable):
    CALLBACK = "callback"
    THREE_D_SECURE_FAILURE = "threeDSecureFailure"
    THREE_D_SECURE_SUCCESS = "threeDSecureSuccess"

    def __init__(self, url, kind=None):
        if kind is None:
            kind = Url.CALLBACK

        self.url = url
        self.kind = kind

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        return Url(dict.get("url", ""), dict.get("kind", ""))
