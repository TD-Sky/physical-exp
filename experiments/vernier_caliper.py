import numpy as np
from collections import namedtuple
from .experiment import Experiment


class Vernier_caliper(Experiment):
    """基本测量-游标卡尺"""

    def __init__(self):
        self.template = "vernier_caliper.txt"
        self.input = "基本测量-游标卡尺.txt"
        self.output = "基本测量-游标卡尺.txt"
        self.data = {}
        self.result = {}
                       

    def collect_data(self):
        """ """
        try:
            raw_data = self.Istream('input', self.input)
        except IOError:
            return -1

        lines = [s for s in raw_data.splitlines() if s != '']
        self.data['D1/mm'] = np.array([float(s) for s in lines[0].split(' ')])
        self.data['H1/mm'] = np.array([float(s) for s in lines[1].split(' ')])


    def process(self):
        """ """
        ChartProperty = namedtuple('ChartProperty', ['S', 'S_x', 'dA', 'dB', 'U_x'])

        for key, val in self.data.items():
            S = val.std(ddof = 1)
            S_x = S / len(val)**0.5
            dA = 2 * S_x
            dB = 0.02
            U_x = (dA ** 2 + dB ** 2)**0.5

            info = ChartProperty(self.round_dec(S, 3),
                                 self.e_format(self.round_dec(S_x, 4)),
                                 self.round_dec(dA, 2),
                                 str(dB),
                                 self.round_dec(U_x, 2))
            self.result[key] = info


    def write_result(self):
        """ """
        self.Ostream('output', self.output, 
                self.toStr('D1/mm', self.result['D1/mm']) + self.toStr('H1/mm', self.result['H1/mm']))


    @staticmethod
    def e_format(number):
        """将小数(字符串)转换成指数形式
        param: str number
        return: str res
        """
        n = float(number)
        return f'{n * 1000} × 10ˉ³'


    @staticmethod
    def toStr(title, achieve):
        """将处理结果转化成字符串
        param: dict achieve
        return: str res
        """
        return (f'{title}\n'
                f'S: {achieve[0]}\n'
                f'S_x: {achieve[1]}\n'
                f'ΔA: {achieve[2]}\n'
                f'ΔB: {achieve[3]}\n'
                f'U_x: {achieve[4]}\n\n')


