import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from .experiment import Experiment
from .tools import getPrefix, round_dec


class Matrl_const():

    def __init__(self, model: LinearRegression):
        self.a: float = float(round_dec(model.intercept_, 3))
        self.k: str = "{} × 10^(-3)".format(
            float(round_dec(-model.coef_[0], 5) * 1000))


class Pn_junction(Experiment):
    """pn结温度-电压特性的测定"""

    def __init__(self):
        self.data: dict = {}
        self.result: Matrl_const

        plt.style.use("classic")
        self.fig = plt.figure()

    def input(self, raw_data: dict):
        self.data["t/C"] = np.array(raw_data["t_C"])
        self.data["U/V"] = np.array(raw_data["U_V"])

    def process(self):
        # 线性回归
        model = LinearRegression(fit_intercept=True)
        reshape_t = self.data["t/C"][:, np.newaxis]
        model.fit(reshape_t, self.data["U/V"])
        Ufit = model.predict(reshape_t)
        self.result = Matrl_const(model)

        # 设置曲线图样式
        plt.xticks(np.arange(25, 80, 5))
        plt.yticks(
            np.arange(
                float(round_dec(self.data["U/V"].min(), 2)),
                float(round_dec(self.data["U/V"].max(), 2)) + 0.01,
                0.01,
            )
        )
        plt.xlabel("t/℃")
        plt.ylabel("U/V")
        plt.grid()

        # 画图
        plt.scatter(self.data["t/C"], self.data["U/V"])
        plt.plot(self.data["t/C"], Ufit)
        self.fig.savefig(
            os.path.join(getPrefix(__file__, -2), "pic", "pn结温度-电压特性的测定.png")
        )

    def output(self) -> str:
        return "a 与 k 是与pn结材料有关的常数\na = {}\nk = {}\n".format(self.result.a, self.result.k)
