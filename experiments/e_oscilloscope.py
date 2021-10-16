import numpy as np
from .tools import round_dec
from .experiment import Experiment


class E_oscilloscope(Experiment):
    "电子示波器的使用"

    def __init__(self):
        self.data: dict
        self.result: dict = {}

    def input(self, raw_data: dict):
        self.data = {
            key: np.array(val) for key, val in raw_data.items() if key != "nodes_ratio"
        }
        self.data["nodes_ratio"] = raw_data["nodes_ratio"]

    def process(self):
        self.result["period"] = np.divide(
            self.data["complete_waves"] * self.data["x_intervals"],
            self.data["frequency"],
        )
        self.result["peak_peak"] = (
            self.data["y_intervals"] * self.data["voltage_konb_gear"]
        )

        effect_vals = np.divide(self.result["peak_peak"], 8 ** 0.5)
        self.result["effect_vals"] = [str(round_dec(n, 2)) for n in effect_vals]

        self.result["correct_factors"] = np.absolute(
            self.data["cal_vals"] - self.data["indicate_vals"]
        )

    def output(self) -> str:
        return "周期: {}\n峰-峰值: {}\n有效值: {}\n修正值: {}\n".format(
            self.result["period"],
            self.result["peak_peak"],
            self.result["effect_vals"],
            self.result["correct_factors"],
        )
