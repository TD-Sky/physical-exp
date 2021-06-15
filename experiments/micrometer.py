import numpy as np
from .experiment import Experiment


class Micrometer(Experiment):
    """基本测量-千分尺"""

    def __init__(self):
        self.template = "micrometer.txt"
        self.io = "基本测量-千分尺"
        self.data = None
        self.result = 0


    def collect_way(self, raw_data):
        """ """
        self.data = np.array(raw_data["diameter"])


    def process(self):
        """ """
        self.result = float(self.round_dec(self.data.mean(), 3))


    def write_result(self):
        """ """
        self.Ostream(f'钢珠直径的平均值 D2/mm ：{self.result}\n')

