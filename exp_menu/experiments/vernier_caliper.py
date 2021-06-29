import numpy as np
from collections import namedtuple
from .experiment import Experiment


class Vernier_caliper(Experiment):
    """基本测量-游标卡尺"""

    def __init__(self):
        self.template = "vernier_caliper.txt"
        self.io = "基本测量-游标卡尺"
        self.data = {}
        self.result = {}
                       

    def collect_way(self, raw_data):
        """ """
        self.data['D1/mm'] = np.array(raw_data["D1/mm"])
        self.data['H1/mm'] = np.array(raw_data["H1/mm"])


    def process(self):
        """ """
        ChartProperty = namedtuple('ChartProperty', ['S', 'S_x', 'dA', 'dB', 'U_x'])

        for key, val in self.data.items():
            S = val.std(ddof = 1)
            S_x = S / len(val)**0.5
            dA = 2 * S_x
            dB = 0.02
            U_x = (dA ** 2 + dB ** 2)**0.5

            self.result[key] = ChartProperty(float(self.round_dec(S, 3)),
                                 f"{float(self.round_dec(S_x, 4)) * 1000} × 10ˉ³",
                                 float(self.round_dec(dA, 2)),
                                 str(dB),
                                 float(self.round_dec(U_x, 2)))


    def write_result(self):
        """ """
        self.Ostream(Vernier_caliper.toStr('D1/mm', self.result['D1/mm']) +
                     Vernier_caliper.toStr('H1/mm', self.result['H1/mm']))


    @staticmethod
    def toStr(title, result):
        """将处理结果转化成字符串
        param: dict result
        return: str s
        """
        return (f'{title}\n'
                f'S: {result[0]}\n'
                f'S_x: {result[1]}\n'
                f'ΔA: {result[2]}\n'
                f'ΔB: {result[3]}\n'
                f'U_x: {result[4]}\n\n')

