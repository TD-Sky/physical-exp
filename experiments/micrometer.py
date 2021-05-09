import numpy as np
from .experiment import Experiment


class Micrometer(Experiment):
    """基本测量-千分尺"""

    def __init__(self):
        self.template = "template/micrometer.txt"
        self.input = "input/基本测量-千分尺.txt"
        self.output = "output/基本测量-千分尺.txt"
        self.data = []
        self.result = 0


    def collect_data(self):
        """ """
        try:
            raw_data = self.Istream(self.input)
        except IOError:
            return -1

        words = raw_data.strip().split(' ')
        self.data = np.array([float(s) for s in words])

        return 0


    def write_result(self):
        """ """
        self.Ostream(self.output, f'钢珠直径的平均值 D2/mm ：{self.result}\n')


    def process(self):
        """ """
        self.result = self.round_dec(self.data.mean(), 3)


