from math import pi as PI
from .tools import round_dec
from .experiment import Experiment


class Moment_of_inertia(Experiment):
    """转动惯量测量"""

    def __init__(self):
        self.data = {}
        self.result = {}

    def input(self, raw_data: dict):
        self.data["h_avg/m"] = raw_data["h_avg_cm"] * 10**(-2)

        self.data["R"] = raw_data["R"] * 10**(-2)
        self.data["r"] = raw_data["r"] * 10**(-2)

        self.data["m_tray/kg"] = raw_data["m_tray_g"] * 10**(-3)
        self.data["m_ring/kg"] = raw_data["m_ring_g"] * 10**(-3)

        self.data["T_i"] = raw_data["T_i"]

    def process(self):
        J_tray = ((self.data["m_tray/kg"] * 9.8 * self.data["R"]
                   * self.data["r"]) / (4 * PI**2 * self.data["h_avg/m"])) * self.data["T_i"][0]**2
        J_ring = (((self.data["m_tray/kg"] + self.data["m_ring/kg"]) * 9.8 * self.data["R"]
                  * self.data["r"]) / (4 * PI**2 * self.data["h_avg/m"])) * self.data["T_i"][1]**2 - J_tray
        J0 = 0.5 * self.data["m_tray/kg"] * self.data["R"]**2
        E = ((J_tray - J0) / J0) * 100

        self.result["J_tray"] = self.J_str(J_tray)
        self.result["J_ring"] = self.J_str(J_ring)
        self.result["J0"] = self.J_str(J0)
        self.result["E"] = "{}%".format(round_dec(E, 1))

    def J_str(self, J: float) -> str:
        return "{} x 10^(-3) kg·m^2".format(round_dec(J * 10**3, 4))

    def output(self) -> str:
        return "悬盘转动惯量测量值: {}\n圆环转动惯量测量值: {}\n空载圆盘转动惯量理论值: {}\n空载圆盘转动惯量的实验误差百分量: {}\n".format(self.result["J_tray"], self.result["J_ring"], self.result["J0"], self.result["E"])
