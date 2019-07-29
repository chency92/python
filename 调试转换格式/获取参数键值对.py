def url_path():
    r = str(input("请输入json格式字典:"))
    d = {str(t).split('=')[0]:str(t).split('=')[1] for t in r.split("&")}
    # print(d)
    print(str(d).replace("'",'"'))


if __name__ == '__main__':
    url_path()