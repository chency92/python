import json
from uuid import uuid1
from requests import Request, Session
from urllib import parse
import urllib

from base64 import b64encode
import hashlib
import hmac
import time
accessKeyId = "5637b8149b5445abbcbc37a8f145ce1c"
accessKeySecret = "2397704d390a437f97b53ff5c40f4df4"


class Test:
    def __init__(self):
        self.headers = {}


    def run(self):
        data = {"phone":"望天7","mac":"805EC0484B28","modelId":"740b5620916a4d0a9a45171630076528","regionId":"e89adb4d568c4c4fb474832953d57904","staffIds":None,"staffs":None,"id":None,"machineId":"2152018111201473"}
        body_md5 = b64encode(hashlib.md5(str(data).encode()).digest()).decode()
        print("body_md5:",body_md5)
        header_add_tuple = (("Content-MD5", body_md5), ("X-Ca-Key", accessKeyId),
                                    ("X-Ca-Nonce", str(uuid1())), ("X-Ca-Timestamp", str(int(1000 * time.time()))))
        headersToSign = ""
        for key, value in header_add_tuple:
            if value:
                self.headers[key] = value

                if headersToSign:
                    headersToSign += "\n"
                headersToSign += key + ":" + value
        stringToSign = "\n".join(["POST", headersToSign, "/api/open/v1/manager/device/add"])
        print("stringToSign是：", stringToSign)
        params_str = ""
        if params_str:
            stringToSign += "\n" + params_str
        ca_signature = b64encode(
            hmac.new(accessKeySecret.encode(), stringToSign.encode(), digestmod=hashlib.sha256).digest()).decode()
        self.headers["X-Ca-Signature"] = ca_signature
        print(self.headers)


if __name__ == '__main__':
    t = Test()
    t.run()