import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from collections import namedtuple
from .experiment import Experiment


class Pn_junction(Experiment):
    """pn结温度-电压特性的测定"""

    def __init__(self):
        self.template = "pn_junction.txt"
        self.io = "pn结温度-电压特性的测定"
        self.data = {}
        self.result = None

        plt.style.use('classic')
        self.fig = plt.figure()
        self.Ufit = None
    

    def collect_way(self, raw_data):
        """ """
        self.data['t/C'] = np.array(raw_data["t/C"])
        self.data['U/V'] = np.array(raw_data["U/V"])


    def process(self):
        """ """
        Matrl_const = namedtuple('Matrl_const', ['a', 'k'])
        # 线性回归
        model = LinearRegression(fit_intercept=True)
        reshape_t = self.data['t/C'][:, np.newaxis]
        model.fit(reshape_t, self.data['U/V'])
        self.Ufit = model.predict(reshape_t)
        self.result = Matrl_const(self.round_dec(model.intercept_, 3),
                    f'{self.round_dec(-model.coef_[0], 5) * 1000} × 10ˉ³')

        # 设置曲线图样式
        plt.xticks(np.arange(25, 80, 5))
        plt.yticks(np.arange(self.round_dec(self.data['U/V'].min(), 2),
                             self.round_dec(self.data['U/V'].max(), 2)+0.01,
                             0.01))
        plt.xlabel('t/℃')
        plt.ylabel('U/V')
        plt.grid()


    def write_result(self):
        """ """
        self.Ostream("a 与 k 是与pn结材料有关的常数\n"
                    f"a = {self.result[0]}\n"
                    f"k = {self.result[1]}\n")

        plt.scatter(self.data['t/C'], self.data['U/V'])
        plt.plot(self.data['t/C'], self.Ufit)
        self.fig.savefig(os.path.join(self.getPrefix(), 'output', 'pn结温度-电压特性的测定.png'))

