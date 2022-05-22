import json
import decimal

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

class ResponseOutCustom:
    def __init__(self, message_id=None, status=None, list_data=None, **kwargs):
        self.message_id = message_id
        self.status = status
        self.list = list_data

        # accept any dict with kwargs
        self.__dict__.update(kwargs)
        if 'transaksi_header' in kwargs:
            self.transaksi_header = kwargs.get("transaksi_header")

    def json(self):
        out_json = {
            "message_id": self.message_id,
            "status": self.status,
            "list": self.list
        }
        return json.dumps(out_json, cls=JSONEncoder)

    def dict(self):
        out_dict = {
            "message_id": self.message_id,
            "status": self.status,
            "list": row2dict(self.list)
        }
        return out_dict

    def failed_resp(self, custom_message=None):
        self.message_id = "01"
        self.status = custom_message if custom_message is not None else "Failed, something went wrong..."
