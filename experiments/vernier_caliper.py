import numpy as np
from collections import namedtuple
from .experiment import Experiment
from .tools import round_dec


class Vernier_caliper(Experiment):
    """基本测量-游标卡尺"""

    def __init__(self):
        self.data = {}
        self.result = {}

    def input(self, raw_data: dict):
        self.data['D1/mm'] = np.array(raw_data["D1_mm"])
        self.data['H1/mm'] = np.array(raw_data["H1_mm"])

    def process(self):
        ChartProperty = namedtuple('ChartProperty', ['S', 'S_x', 'dA', 'dB', 'U_x'])

        for key, val in self.data.items():
            S = val.std(ddof = 1)
            S_x = S / len(val)**0.5
            dA = 2 * S_x
            dB = 0.02
            U_x = (dA ** 2 + dB ** 2)**0.5

            self.result[key] = ChartProperty(float(round_dec(S, 3)),
                                 f"{float(round_dec(S_x, 4)) * 1000} × 10ˉ³",
                                 float(round_dec(dA, 2)),
                                 str(dB),
                                 float(round_dec(U_x, 2)))

    def res_str(self, title: str, result: dict) -> str:
        """将处理结果转化成字符串"""
        return (f'{title}\n'
                f'S: {result[0]}\n'
                f'S_x: {result[1]}\n'
                f'ΔA: {result[2]}\n'
                f'ΔB: {result[3]}\n'
                f'U_x: {result[4]}\n'
                '\n')

    def output(self) -> str:
        return self.res_str('D1/mm', self.result['D1/mm']) + self.res_str('H1/mm', self.result['H1/mm'])
