import json


class RedeSerializable:
    def to_json(self):
        return json.dumps(self.serialize(), cls=RecursiveEncoder)

    def serialize(self):
        dict = {k: v for k, v in self.__dict__.items() if v is not None}

        for k, v in dict.items():
            if hasattr(v, "serialize"):
                dict[k] = v.serialize()

        return dict


class RecursiveEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'serialize'):
            return obj.serialize()
        else:
            return json.JSONEncoder.default(self, obj)
