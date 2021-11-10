from math import pi as PI
from .tools import round_dec
from .experiment import Experiment


class Young_modulus(Experiment):
    """杨氏模量的测量"""

    def __init__(self):
        self.data = {}
        self.result = {}

    def input(self, raw_data: dict):
        self.data["b/m"] = raw_data["b_m"]
        self.data["L/m"] = raw_data["L_m"]
        self.data["D/m"] = raw_data["D_m"]
        self.data["d/m"] = raw_data["d_mm"] * 10**(-3)
        self.data["n_avg/mm"] = raw_data["n_avg_mm"]
        self.data["dm/kg"] = raw_data["dm_kg"]

    def process(self):
        self.result["dn/mm"] = [self.data["n_avg/mm"][r] - self.data["n_avg/mm"][l]
                                for l, r in zip(range(0, 4), range(4, 8))]
        dn_avg_m: float = sum(self.result["dn/mm"]) * 10**(-3) / 4
        E: float = (8 * self.data["D/m"] * self.data["L/m"] * self.data["dm/kg"]
                    * 9.8) / (PI * self.data["d/m"]**2 * self.data["b/m"] * dn_avg_m)
        self.result["E"] = round_dec(E * 10**(-11), 4)

    def output(self) -> str:
        return "偏移量逐差: {}\n杨氏模量E = {} x 10^(-11) Pa\n".format(self.result["dn/mm"], self.result["E"])
