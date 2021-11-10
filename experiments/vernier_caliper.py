import numpy as np
from .experiment import Experiment
from .tools import round_dec


class ChartProperty():
    def __init__(self, S, S_x, dA, dB, U_x):
        self.S = round_dec(S, 3)
        self.S_x = round_dec(S_x * 10**3, 4)
        self.dA = round_dec(dA, 2)
        self.dB = dB
        self.U_x = round_dec(U_x, 2)

    def res_str(self, title: str) -> str:
        return "{}\nS: {}\nS_x: {} x 10^(-3)\nΔA: {}\nΔB: {}\nU_x: {}\n".format(
            title, self.S, self.S_x, self.dA, self.dB, self.U_x) + '\n'


class Vernier_caliper(Experiment):
    """基本测量-游标卡尺"""

    def __init__(self):
        self.data = {}
        self.result = {}

    def input(self, raw_data: dict):
        self.data['D1/mm'] = np.array(raw_data["D1_mm"])
        self.data['H1/mm'] = np.array(raw_data["H1_mm"])

    def process(self):
        for key, val in self.data.items():
            S = val.std(ddof=1)
            S_x = S / len(val)**0.5
            dA = 2 * S_x
            dB = 0.02
            U_x = (dA ** 2 + dB ** 2)**0.5
            self.result[key] = ChartProperty(S, S_x, dA, dB, U_x)

    def output(self) -> str:
        return self.result["D1/mm"].res_str('D1/mm') + self.result["H1/mm"].res_str('H1/mm')
