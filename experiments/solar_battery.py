import os
import matplotlib.pyplot as plt
import numpy as np
from .experiment import Experiment


class Solar_battery(Experiment):
    """太阳能电池基本特性的测量"""

    def __init__(self):
        self.template = "solar_battery.txt"
        self.io = "太阳能电池基本特性的测量.txt"
        self.data = {}
        self.result = {}

        plt.style.use('classic')
        self.fig = plt.figure()
    

    def collect_data(self):
        """ """
        code = 0
        try:
            raw_data = self.Istream('input', self.io)
        except IOError:
            code = -1
        else:
            lines = [ line.split() for line in raw_data.splitlines() if line != '' ]
            cols = list(zip(*lines))
            self.data['R'] = tuple([ int(s) for s in cols[0] ])
            self.data['I/mA'] = np.array([ float(s) for s in cols[1] ])
            self.data['U/V'] = np.array([ float(s) for s in cols[2] ])


    def process(self):
        """ """
        Ps = [ I*U for I, U in zip(self.data['I/mA'], self.data['U/V']) ]
        self.result['P/mW'] = [self.round_dec(P, 3) for P in Ps]

        # 设置曲线图样式
        plt.xticks(np.arange(0, 3, 0.1))
        plt.yticks(np.arange(0, 3, 0.1))
        plt.grid()
        plt.scatter(self.data['U/V'], self.data['I/mA'])


    def write_result(self):
        """ """
        # 获取 最大输出功率及相应电阻值
        # 与 绘制电阻-功率表格 二合一
        R_P = 'R/Ω\t\tP/mW\n'
        Pmax = cores_R = 0
        for R, P in zip(self.data['R'], self.result['P/mW']):
            R_P += f'{R}\t\t{self.round_dec(P, 3)}\n'
            if Pmax < P:
                Pmax = P
                cores_R = R
        else:
            R_P += '\n'

        self.Ostream('output', self.io,
                R_P + 
                f"最大输出功率: {self.round_dec(Pmax, 3)}\n" + 
                f"相应电阻值: {cores_R}\n"
                "手算填充因子，请：\n\n")

        self.fig.savefig(os.path.join(self.getPrefix(), 'output', '太阳能电池伏安特性曲线.png'))

