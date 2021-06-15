import os
import numpy as np
import matplotlib.pyplot as plt
from .experiment import Experiment
from pprint import pprint


class Non_linear(Experiment):
    "非线性实验"

    def __init__(self):
        self.template = "non_linear.txt"
        self.io = "非线性实验"
        self.data = None
        self.result = {}

        plt.style.use('classic')
        self.result["ord_diode"] = plt.figure(figsize=(12, 12))
        self.result["zener_diode"] = plt.figure(figsize=(12, 12))
        self.result["light_diode"] = plt.figure(figsize=(12, 12))


    def collect_way(self, raw_data):
        """ """
        self.data = Non_linear.set_np(raw_data)


    def write_result(self):
        """ """
        pass


    @staticmethod
    def set_np(dct):
        """传入一个字典，若其值为数组，则设为numpy数组
        param: dict dct
        return: dict res
        """
        for key, val in dct.items():
            if isinstance(val, dict):
                dct[key] = Non_linear.set_np(val)
            else:
                dct[key] = np.array(val)
        return dct


    @staticmethod
    def set_graph(dct):
        """设置曲线图样式"""
        ax = plt.gca()

        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

        ax.set_xticks([-1.2, 1.2])
        ax.set_yticks([-1.2, 1.2])

        plt.xticks(np.arange(0, float(self.round_dec(self.data['U/V'].max(), 1))+0.1, 0.1))
        plt.yticks(np.arange(0, float(self.round_dec(self.data['I/mA'].max(), 1))+0.1, 0.1))
        plt.xlabel('U/V')
        plt.ylabel('I/mA')
        plt.grid()

