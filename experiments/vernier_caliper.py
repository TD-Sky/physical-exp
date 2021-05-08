import numpy as np
from .experiment import Experiment


class Vernier_caliper(Experiment):
    """基本测量-游标卡尺"""

    def __init__(self):
        self.template = "template/vernier_caliper.txt"
        self.input = "input/基本测量-游标卡尺.txt"
        self.output = "output/基本测量-游标卡尺.txt"
        self.data = {}
        self.result = {'D1/mm': {}, 'H1/mm': {}}
                       

    def collect_data(self):
        """ """
        try:
            raw_data = self.Istream(self.input)
        except IOError:
            return -1

        lines = [s for s in raw_data.split('\n') if s != '']
        self.data['D1/mm'] = np.array([float(s) for s in lines[0].split(' ')])
        self.data['H1/mm'] = np.array([float(s) for s in lines[1].split(' ')])


    def process(self):
        """ """
        for key, val in self.data.items():
            S = val.std(ddof = 1)
            S_x = S / len(val)**0.5
            dA = 2 * S_x
            dB = 0.02
            self.result[key]['S'] = self.round_dec(S, 3)
            self.result[key]['S_x'] = self.round_dec(S_x, 4)
            self.result[key]['dA'] = self.round_dec(dA, 2)
            self.result[key]['dB'] = str(dB)
            self.result[key]['U_x'] = self.round_dec((dA ** 2 + dB ** 2)**0.5, 2)


    def write_result(self):
        """ """
        self.Ostream(self.output, self.toStr('D1/mm', self.result['D1/mm']) + self.toStr('H1/mm', self.result['H1/mm']))


    def toStr(self, title, achieve):
        """将处理结果转化成字符串
        param: dict achieve
        return: str res
        """
        return f"{title}\nS: {achieve['S']}\nS_x: {achieve['S_x']}\t(手写成×10^(-3)形式)\nΔA: {achieve['dA']}\nΔB: {achieve['dB']}\nU_x: {achieve['U_x']}\n\n"


