import numpy as np
from .experiment import Experiment


class Micrometer(Experiment):
    """基本测量-千分尺"""

    def __init__(self):
        self.template = "template/micrometer.txt"
        self.input = "input/基本测量-千分尺.txt"
        self.data = []
        self.result = 0


    def collect_data(self):
        """ """
        code = 0
        try:
            raw_data = self.Istream(self.input)
        except IOError:
            code = -1

        words = raw_data.strip().split(' ')
        self.data = np.array([float(s) for s in words])

        return code


    def write_result(self):
        """ """
        self.Ostream("output/基本测量-千分尺.txt", f'钢珠直径的平均值 D2/mm ：{self.result:.3f}\n')


    def process(self):
        """ """
        self.result = self.data.mean()


