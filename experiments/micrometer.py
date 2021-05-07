from .experiment import Experiment


class Micrometer(Experiment):
    """基本测量-千分尺"""


    def __init__(self):
        self.template = "template/micrometer.txt"
        self.data = None
        self.result = 0


    def read_data(self):
        """ """
        file = self.set_path("input/基本测量-千分尺.txt")
        with open(file, 'r') as fp:
            words = fp.read().strip().split(' ')
        self.data = [float(word) for word in words]


    def write_result(self):
        """ """
        file = self.set_path("output/基本测量-千分尺.txt")
        with open(file, 'w') as fp:
            fp.write(f'钢珠直径的平均值 D2/mm ：{self.result:.3f}\n')


    def process(self):
        """ """
        self.result = sum(self.data) / len(self.data)


