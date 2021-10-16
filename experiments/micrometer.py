import numpy as np
from .tools import round_dec
from .experiment import Experiment


class Micrometer(Experiment):
    """基本测量-千分尺"""

    def __init__(self):
        self.data: np.ndarray
        self.result = 0

    def input(self, raw_data: dict):
        self.data = np.array(raw_data["diameter"])

    def process(self):
        self.result = float(round_dec(self.data.mean(), 3))

    def output(self) -> str:
        return f"钢珠直径的平均值 D2/mm ：{self.result}\n"
