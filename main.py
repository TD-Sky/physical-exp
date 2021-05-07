import os
import sys
import experiments as exps


def choose():
    """让用户选择实验类型，对错误输入作出响应
    成功码为0，数字错误码为1，非法输入码为-1
    param: None
    return: int exp_t, int code
    """
    exp_t = -1
    code = 0
    choice = input("请选择实验类型：")

    try:
        n = int(choice)
    except ValueError:
        code = -1

    if n < 0 or n > 2: 
        code = 1
    else:
        exp_t = n

    return exp_t, code


def interact():
    """交互逻辑"""
    exp_tuple = (exps.Micrometer, exps.Vernier_caliper)

    while True:
        os.system('clear')

        print("0) 基本测量-千分尺\n1) 基本测量-游标卡尺\n2) 退出程序")
        exp_t, code = choose()

        if code != 0:

            if code == 1:
                print("请输入菜单给出的数字！")
            elif code == -1:
                print("请正确输入！")

            continue

        if exp_t == 2:
            sys.exit()

        exp = exp_tuple[exp_t]()
        exp.print_template()
        exp.collect_data()



if __name__ == '__main__':
    interact()

