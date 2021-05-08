import os
import sys
import experiments as exps


def choose():
    """让用户选择实验类型，对错误输入作出响应
    成功码为0，非法输入码为-1
    param: None
    return: int exp_t, int code
    """
    n = -1
    code = 0
    choice = input("请选择实验类型：")

    try:
        n = int(choice)
    except ValueError:
        code = -1

    exp_t = n

    return exp_t, code


def interact():
    """交互逻辑"""
    exp_tuple = (exps.Micrometer, exps.Vernier_caliper)

    while True:
        os.system('clear')

        print("1) 基本测量-千分尺\n2) 基本测量-游标卡尺\n0) 退出程序")
        exp_t, code = choose()

        if code == -1:
            print("\n请输入菜单选项编号！")
            input("\n按任意键继续")
            continue

        if exp_t == 0:
            sys.exit()

        exp = exp_tuple[exp_t - 1]()
        exp.print_template()
        exp.collect_data()
        exp.process()
        exp.write_result()
        input("\n按任意键继续")



if __name__ == '__main__':
    interact()

