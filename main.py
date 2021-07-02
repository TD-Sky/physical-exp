import os
import sys
from exp_menu import ExpMenu
from getpass import getpass


def choose():
    """让用户选择实验类型，对错误输入作出响应
    成功码为0，非法输入码为-1
    param: None
    return: int exp_t, int code
    """
    exp_t = -1
    code = 0
    option = input("请选择实验类型：")

    try:
        n = int(option)
    except ValueError:
        code = -1
    else:
        if (0 <= n <= 7):
            exp_t = n
        else:
            code = -1

    return exp_t, code


def interact():
    """交互逻辑"""
    exp_menu = ExpMenu()
    clr_scr = "clear" if sys.platform == "linux" else "cls"

    while True:
        os.system(clr_scr)

        print("1) 基本测量-千分尺\n"
              "2) 基本测量-游标卡尺\n"
              "3) 太阳能电池基本特性的测量\n"
              "4) pn结温度-电压特性的测定\n"
              "5) 电子示波器的使用\n"
              "6) 牛顿环实验\n"
              "7) 非线性实验(废案)\n"
              "0) 退出程序")
        exp_t, code = choose()

        if code == -1:
            getpass("\n请输入菜单选项编号！\n\n按回车键继续")
            continue

        if exp_t == 0:
            os.system(clr_scr)
            sys.exit()

        exp_menu.choose(exp_t-1)
        exp_menu.using.print_template()
        getpass("\n请先放入文件，再按回车键继续")

        flag = exp_menu.using.collect_data()
        if flag == 0:
            try:
                exp_menu.using.process()
            except KeyError:
                getpass("\n某段输入数据的名字写错了\n\n回车键继续")
            else:
                exp_menu.using.write_result()
                getpass("\n结果已经写入至 output 目录中\n\n回车键继续")
            finally:
                exp_menu.remake()
        elif flag == 1:
            getpass("\n未找到正确的输入文件！\n\n回车键继续")
        elif flag == 2:
            getpass("\n输入内容格式错误！\n\n回车键继续")


if __name__ == '__main__':
    interact()

