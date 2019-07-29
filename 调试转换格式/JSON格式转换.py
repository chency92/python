def ch_json():
    r = input("请输入json格式字典:")
    print(str(r).replace("true", "True").replace("null", "None").replace("false", "False").replace(",", ",\n "))
    # return print(r.replace("true", "True").replace("null", "None").replace("false", "False"))


if __name__ == '__main__':
    ch_json()
