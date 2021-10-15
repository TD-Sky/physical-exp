# 因问题太复杂，导致该模块成为废案

import os
import numpy as np
import matplotlib.pyplot as plt
from .experiment import Experiment
from .tools import round_dec


class Non_linear(Experiment):
    "非线性实验"

    def __init__(self):
        self.data = None
        self.result = {}

        plt.style.use('classic')
        self.result["ord_diode"] = plt.figure(figsize=(12, 12))
        self.result["zener_diode"] = plt.figure(figsize=(12, 12))
        self.result["light_diode"] = plt.figure(figsize=(12, 12))

    def input(self, raw_data: dict):
        self.data = self.set_np(raw_data)

    def set_np(self, dct: dict):
        """传入一个字典，若其值为数组，则设为numpy数组"""
        for key, val in dct.items():
            dct[key] = self.set_np(val) if isinstance(val, dict) else np.array(val)

    def set_graph(self, dct):
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

        plt.xticks(np.arange(0, float(round_dec(self.data['U_V'].max(), 1))+0.1, 0.1))
        plt.yticks(np.arange(0, float(round_dec(self.data['I_mA'].max(), 1))+0.1, 0.1))
        plt.xlabel('U/V')
        plt.ylabel('I/mA')
        plt.grid()

