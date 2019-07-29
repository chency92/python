def num_1(number):
    for i in range(number):
        print("w", end="")
    print()


def cha_1():
    cha = input("请输入：")
    print(len(cha))


def li_print():
    t1 = input('请输入：')
    for i in range(1, 200):
        with open("用例编号.txt", "a", encoding="utf-8") as f:
            if i < 10:
                print(f"{t1}00{i}")
                f.write(f"{t1}00{i}")
                f.write("\n")
            elif i > 99:
                print(f"{t1}{i}")
                f.write(f"{t1}{i}")
                f.write("\n")
            else:
                print(f"{t1}0{i}")
                f.write(f"{t1}0{i}")
                f.write("\n")


if __name__ == '__main__':
    # num_1(128)
    # cha_1()#
    li_print()