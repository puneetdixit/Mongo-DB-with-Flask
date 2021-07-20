import json

from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    """
    This will be used to convert the ObjectId in json form.
    """

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
