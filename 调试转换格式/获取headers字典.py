def get_headers_dict(d):
    """获取headers字典"""
    headers_dic = {one.split(":")[0].strip(): one.split(":")[1].strip() for one in d.split("\n")}
    print(str(headers_dic).replace(",", ",\n "))
    return headers_dic


if __name__ == '__main__':
    # d = """Access-Control-Allow-Methods: GET, POST, PUT, DELETE, HEAD
    #         Access-Control-Allow-Origin: *
    #         Access-Control-Expose-Headers: etag, x-oss-request-id
    #         Access-Control-Max-Age: 60
    #         Connection: keep-alive
    #         Content-Length: 0
    #         Content-MD5: nRp2SOthPgp65dtY8xd36Q==
    #         Date: Fri, 05 Jul 2019 00:55:49 GMT
    #         ETag: "9D1A7648EB613E0A7AE5DB58F31777E9"
    #         Server: AliyunOSS
    #         x-oss-hash-crc64ecma: 6325834620684950774
    #         x-oss-request-id: 5D1E9FF3EE5BBF43E0F5777D
    #         x-oss-server-time: 289"""
    d = """Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryxY4bgVuqqxvqOzqs
    Origin: https://10.200.112.162
    Referer: https://10.200.112.162/manager/deviceManage/addResource
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"""
    get_headers_dict(d)