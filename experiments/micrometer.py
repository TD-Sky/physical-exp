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
        self.data = [float(s) for s in words]
        print(self.data)

        return code


    def write_result(self):
        """ """
        file = self.set_path("output/基本测量-千分尺.txt")
        with open(file, 'w') as fp:
            fp.write(f'钢珠直径的平均值 D2/mm ：{self.result:.3f}\n')


    def process(self):
        """ """
        self.result = sum(self.data) / len(self.data)


