def add_open():
    r = str(input("接口路径："))
    url_path = "/api/open/" + r.split("api/")[1]
    print(url_path)


if __name__ == '__main__':
    while True:
        add_open()