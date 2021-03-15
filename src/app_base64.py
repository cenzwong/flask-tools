import base64
from flask import request

url_prefix = "/base64"

# /encode?data=1234
def enconde_decode(encode_decode):
    mydata = request.args.get('data')
    if encode_decode == "encode":
        return base64.b64encode(mydata.encode()).decode()
    elif encode_decode == "decode":
        return base64.b64decode(mydata.encode()).decode()
