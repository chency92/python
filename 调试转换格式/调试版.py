import requests
import urllib3
import cfg
from uuid import uuid1
from requests import Request, Session
from urllib import parse
import urllib

from base64 import b64encode
import hashlib
import hmac
import time
from bs4 import BeautifulSoup
import json
import pprint

urllib3.disable_warnings()
accessKeyId = cfg.accessKeyId
accessKeySecret = cfg.accessKeySecret


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
        # print(parsed_url)
        uri = parsed_url.path[1:] if parsed_url.path.startswith("/") else parsed_url.path
        params_str = parsed_url.query
        body = prepped.body

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
            # print("第二次", stringToSign)
        ca_signature = b64encode(
            hmac.new(accessKeySecret.encode(), stringToSign.encode(), digestmod=hashlib.sha256).digest()).decode()
        prepped.headers["X-Ca-Signature"] = ca_signature

        s = Session()
        s.headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.131 Safari/537.36"
        r = s.send(prepped, verify=False)
        return r


class OpenApi:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.headers = {
                        "X-Ca-Key": accessKeyId,
                        "X-Ca-Timestamp": "{{x_ca_timestamp}}",
                        "X-Ca-Nonce": "{{x_ca_nonce}}",
                        "X-Ca-Signature": "{{x_ca_signture}}",
                        "Content-MD5": "{{content_md5}}",
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.131 Safari/537.36"
                        }
        self.url = cfg.URL
        self.session = requests.session()

    def get_baidu(self):
        # url = "https://www.baidu.com/"
        response = requests.get(self.url, headers=self.headers, verify=False)
        # print(response.text)
        print(response.content.decode())
        assert response.status_code == 200
        if "http://www.baidu.com" in response.text:
            return True
        else:
            return False


if __name__ == '__main__':
    open_api = OpenApi()
    # open_api.get_baidu()
