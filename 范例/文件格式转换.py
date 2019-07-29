def ch_text():
    """请求头格式转换"""
    """
    Connection: keep-alive
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    """
    data = input("请输入转换文本：")
    print(data.split("    "))
    li = data.split("\n")
    for i in range(len(li)):
        print(li[i])
        t = str(li[i].split(":")).replace(",", ':')
        print(t)


if __name__ == '__main__':
    ch_text()