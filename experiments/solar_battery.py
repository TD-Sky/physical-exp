import os
import matplotlib.pyplot as plt
import numpy as np
from .experiment import Experiment


class Solar_battery(Experiment):
    """太阳能电池基本特性的测量"""

    def __init__(self):
        self.template = "solar_battery.txt"
        self.io = "太阳能电池基本特性的测量"
        self.data = {}
        self.result = {}

        plt.style.use('classic')
        self.fig = plt.figure(figsize=(12, 12))
    

    def collect_way(self, raw_data):
        """ """
        self.data['R/O'] = tuple(raw_data["R/O"])
        self.data['I/mA'] = np.array(raw_data["I/mA"])
        self.data['U/V'] = np.array(raw_data["U/V"])


    def process(self):
        """ """
        Ps = [ I*U for I, U in zip(self.data['I/mA'], self.data['U/V']) ]
        self.result['P/mW'] = [self.round_dec(P, 3) for P in Ps]

        # 设置曲线图样式
        plt.xticks(np.arange(0, self.round_dec(self.data['U/V'].max(), 1)+0.1, 0.1))
        plt.yticks(np.arange(0, self.round_dec(self.data['I/mA'].max(), 1)+0.1, 0.1))
        plt.xlabel('U/V')
        plt.ylabel('I/mA')
        plt.grid()


    def write_result(self):
        """ """
        # 获取 最大输出功率及相应电阻值
        # 与 绘制电阻-功率表格 二合一
        R_P = f"{'R/Ω':4s}\t\t{'P/mW':4s}\n"
        Pmax = cores_R = 0
        for R, P in zip(self.data["R/O"], self.result['P/mW']):
            R_P += f'{R:4d}\t\t{self.round_dec(P, 3):.3f}\n'
            if Pmax < P:
                Pmax = P
                cores_R = R
        else:
            R_P += '\n'

        self.Ostream(R_P + 
                f"最大输出功率: {self.round_dec(Pmax, 3)}\n"
                f"相应电阻值: {cores_R}\n"
                "手算填充因子，F = Pm/(Isc × Uoc)，请：\n")

        plt.scatter(self.data['U/V'], self.data['I/mA'])
        self.fig.savefig(os.path.join(self.getPrefix(), 'output', '太阳能电池伏安特性曲线.png'))

