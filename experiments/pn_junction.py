import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from .experiment import Experiment


class Pn_junction(Experiment):
    """pn结温度-电压特性的测定"""

    def __init__(self):
        self.template = "pn_junction.txt"
        self.io = "pn结温度-电压特性的测定.txt"
        self.data = {}
        self.result = {}

        plt.style.use('classic')
        self.fig = plt.figure()
        self.Ufit = None
    

    def collect_data(self):
        """ """
        code = 0
        try:
            raw_data = self.Istream('input', self.io)
        except IOError:
            code = -1
        else:
            lines = [ line.split() for line in raw_data.splitlines() if line != '' ]
            self.data['t'] = np.array([int(x) for x in lines[0]])
            self.data['U/V'] = np.array([float(x) for x in lines[1]]) 

        return code


    def process(self):
        """ """
        # 线性回归
        model = LinearRegression(fit_intercept=True)
        reshape_t = self.data['t'][:, np.newaxis]
        model.fit(reshape_t, self.data['U/V'])
        self.Ufit = model.predict(reshape_t)

        # 设置曲线图样式
        plt.xticks(np.arange(25, 80, 5))
        plt.yticks(np.arange(0.5, 0.7, 0.01))
        plt.grid()


    def write_result(self):
        """ """
        plt.scatter(self.data['t'], self.data['U/V'])
        plt.plot(self.data['t'], self.Ufit)
        self.fig.savefig(os.path.join(self.getPrefix(), 'output', 'pn结温度-电压特性的测定.png'))

