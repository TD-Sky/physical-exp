import numpy as np
from .experiment import Experiment


class E_oscilloscope(Experiment):
    "电子示波器的使用"

    def __init__(self):
        self.template = "e_oscilloscope.txt"
        self.io = "电子示波器的使用"
        self.data = None
        self.result = {}
    

    def collect_way(self, raw_data):
        """ """
        self.data = {key: np.array(val) for key, val in raw_data.items() if key != "nodes_ratio"}
        self.data["nodes_ratio"] = raw_data["nodes_ratio"]


    def process(self):
        """ """
        self.result["period"] = np.divide(self.data["complete_waves"] * self.data["x_intervals"], self.data["frequency"])
        self.result["peak_peak"] = self.data["y_intervals"] * self.data["voltage_konb_gear"]
        self.result["effect_vals"] = np.divide(self.result["peak_peak"], 8**0.5)
        self.result["correct_factors"] = np.absolute(self.data["cal_vals"] - self.data["indicate_vals"])

