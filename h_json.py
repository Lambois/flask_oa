from flask import jsonify

class Json(object):
    def __init__(self,code,message,data):
        self.code = code
        self.message = message
        self.data = data

    def h_jsonify(self):
        return jsonify({"code":self.code,"message":self.message,"data":self.data})
    