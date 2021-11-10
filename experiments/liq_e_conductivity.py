import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from .tools import getPrefix, round_dec
from .experiment import Experiment


class Liq_e_conductivity(Experiment):
    """液体电导率的测量"""

    def __init__(self):
        self.data: dict = {}
        self.result: dict = {}

        plt.style.use("classic")
        self.fig = plt.figure(figsize=(12, 12))

    def input(self, raw_data: dict):
        self.data["V_in"] = raw_data["V_in"]
        self.data["V_out"] = np.array(raw_data["V_out"])
        self.data["R"] = np.array(raw_data["R"])
        self.data["V_salt"] = raw_data["V_salt"]
        self.data["L/mm"] = raw_data["L_mm"]
        self.data["S/mm"] = raw_data["S"]

    def process(self):

        self.result["V_OI"] = [str(round_dec(ratio, 3)) for ratio in (
            self.data["V_out"] / self.data["V_in"])]

        V_OI = np.array([float(s) for s in self.result["V_OI"]])
        R_rec = np.array([float(round_dec(rec, 3))
                         for rec in self.data["R"]**(-1)])

        model = LinearRegression(fit_intercept=True)
        reshape_v = V_OI[:, np.newaxis]
        model.fit(reshape_v, R_rec)
        Vfit = model.predict(reshape_v)

        B: float = model.coef_[0]
        K: float = (self.data["L/mm"] / self.data["S/mm"]) * B**(-1)
        ratio_salt = K * (self.data["V_salt"] / self.data["V_in"])

        self.result["K"] = "{}".format(round_dec(K, 3))
        self.result["ratio_salt"] = "{} x 10^(-3)".format(
            round_dec(ratio_salt * 10**(3), 3))

        # 设置曲线图样式
        plt.xticks(np.arange(V_OI.min(), V_OI.max() + 0.1, 0.02))
        plt.yticks(np.arange(R_rec.min(), R_rec.max() + 0.1, 0.03))
        plt.xlabel("V_OI")
        plt.ylabel("R^(-1)")
        plt.grid()

        # 画图
        plt.scatter(V_OI, R_rec)
        plt.plot(V_OI, Vfit)
        self.fig.savefig(
            os.path.join(getPrefix(__file__, -2), "pic", "液体电导率的测量.png")
        )

    def output(self) -> str:
        return "V_out/V_in 列表: {}\nK值: {}\n食盐水电导率: {} s/mm\n".format(self.result["V_OI"], self.result["K"], self.result["ratio_salt"])
