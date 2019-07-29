import json
import pprint
from uuid import uuid1
from requests import Request, Session
from urllib import parse
import urllib

from base64 import b64encode
import hashlib
import hmac
import time

# import re

accessKeyId = "5637b8149b5445abbcbc37a8f145ce1c"
accessKeySecret = "2397704d390a437f97b53ff5c40f4df4"


# RPS 鉴权码
# accessKeyId = '8d1422c11c6e443ab24c2bdc26651353'
# accessKeySecret = 'ad51add0332b4008a1a9abfef224fdbc'

# 127 环境告警API
# accessKeyId = '6bc4a7b6febd4d88921eed50998f2f34'
# accessKeySecret = 'c00cbb56c3694ec6a198732b7fbaadb0'

# onl 鉴权
# accessKeyId = '486055919c1142c3a8efdf261ba1f446'
# accessKeySecret = '8c4e73857ef940399175a8da866b8664'

# s = Session()
# req = Request("get", url="http://www.baidu.com/123", data={"1": "1", "3":"3"}, json={"2":"2"})
# prepped = req.prepare()
#
# print(prepped.method)
# print(prepped.body)
# prepped.headers["1"] = "1"
# print(prepped.url)
# print(parse.urlparse(prepped.url))
#
# s.send(prepped)


class Rrequests(object):
    def __init__(self, *args, **kwargs):
        self.req = Request(*args, **kwargs)
        self.url = kwargs.get("url", None) or args[1]
        self.data = kwargs.get("data", None)
        self.json = kwargs.get("json", None)

    def send(self):
        prepped = self.req.prepare()

        method = prepped.method
        url = urllib.parse.unquote(prepped.url)
        # print(method)
        # 拆分URL
        parsed_url = parse.urlparse(url)
        print(parsed_url)
        # 获取URL path
        uri = parsed_url.path[1:] if parsed_url.path.startswith("/") else parsed_url.path
        # print("这是URI",uri)
        params_str = parsed_url.query
        # print("这是params_str", params_str)
        body = prepped.body
        # print("这是body",body)

        if self.json:
            body_md5 = b64encode(hashlib.md5(body).digest()).decode()
        else:
            body_md5 = None

        header_add_tuple = (("Content-MD5", body_md5), ("X-Ca-Key", accessKeyId),
                            ("X-Ca-Nonce", str(uuid1())), ("X-Ca-Timestamp", str(int(1000 * time.time()))))

        headersToSign = ""

        for key, value in header_add_tuple:
            if value:
                prepped.headers[key] = value

                if headersToSign:
                    headersToSign += "\n"
                headersToSign += key + ":" + value

        stringToSign = "\n".join([method, headersToSign, uri])
        # print("stringToSign是：", stringToSign)

        if params_str:
            stringToSign += "\n" + params_str
            # print("第二次stringToSign是：", stringToSign, type(stringToSign))
        # print("==========================")
        ca_signature = b64encode(
            hmac.new(accessKeySecret.encode(), stringToSign.encode(), digestmod=hashlib.sha256).digest()).decode()
        prepped.headers["X-Ca-Signature"] = ca_signature
        # print("请求headers",prepped.headers)
        s = Session()
        s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, " \
                                  "like Gecko)Chrome/74.0.3729.131 Safari/537.36 "
        r = s.send(prepped, verify=False)
        return r


if __name__ == "__main__":
    base_url = 'http://10.200.110.172:9989'
    # x = Rrequests("get", url=base_url + "/api/open/v1/manager/device/getDetail",
    #               params={"id": "e8433e3856164634bfdeebc2e78ab0ca"})
    # r = x.send()
    # pprint.pprint(r.json(), indent=2)
    # json_data = json.loads(json.loads(r.text)["data"])[0]["children"][0]["children"]
    # # print(type(json_data))
    # mac_info = {str(j).split(":")[0]: str(j).split(":")[1].strip() for j in [i['label'] for i in json_data]}
    # print(mac_info)
    data = {"phone":"2334","mac":"805ec0484b21","modelId":"740b5620916a4d0a9a45171630076528","regionId":"e89adb4d568c4c4fb474832953d57904","staffIds":None,"staffs":None,"id":None,"machineId":"2152018111201473"}
    x = Rrequests("post", url= base_url + "/api/open/v1/manager/device/add",
                  json=data)
    r = x.send()
    print(r.json())

