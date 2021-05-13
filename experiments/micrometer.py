import numpy as np
from .experiment import Experiment


class Micrometer(Experiment):
    """基本测量-千分尺"""

    def __init__(self):
        self.template = "micrometer.txt"
        self.io = "基本测量-千分尺.txt"
        self.data = None
        self.result = 0


    def collect_way(self, raw_data):
        """ """
        words = raw_data.strip().split()
        self.data = np.array([float(s) for s in words if s != ''])


    def write_result(self):
        """ """
        self.Ostream('output', self.io, f'钢珠直径的平均值 D2/mm ：{self.result}\n')


    def process(self):
        """ """
        self.result = self.round_dec(self.data.mean(), 3)


