import os
import sys
import experiments as exps
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
        if (0 <= n <= 3):
            exp_t = n
        else:
            code = -1

    return exp_t, code


def interact():
    """交互逻辑"""
    command = 'clear' if sys.platform == 'linux' else 'cls'

    exp_tuple = (exps.Micrometer, 
                 exps.Vernier_caliper,
                 exps.Solar_battery)

    while True:
        os.system(command)

        print("1) 基本测量-千分尺\n"
              "2) 基本测量-游标卡尺\n"
              "3) 太阳能电池基本特性的测量\n"
              "0) 退出程序")
        exp_t, code = choose()

        if code == -1:
            getpass("\n请输入菜单选项编号！\n\n按回车键继续")
            continue

        if exp_t == 0:
            os.system('clear')
            sys.exit()

        exp = exp_tuple[exp_t - 1]()

        exp.print_template()
        getpass("\n请先放入文件，再按回车键继续")

        if exp.collect_data() == -1:
            getpass("\n未找到正确的输入文件！\n\n回车键继续")
            continue

        exp.process()
        exp.write_result()
        getpass("\n结果已经写入至 output 目录中\n\n回车键继续")



if __name__ == '__main__':
    interact()

