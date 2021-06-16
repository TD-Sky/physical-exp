import numpy as np
from .experiment import Experiment

class Newton_ring(Experiment):
    """牛顿环实验"""

    def __init__(self):
        self.template = "newton_ring.txt"
        self.io = "牛顿环实验"
        self.data = None
        self.result = {}


    def collect_way(self, raw_data):
        """ """
        self.data = {key: np.array(val) for key, val in raw_data.items()}


    def process(self):
        """ """
        self.result["D"] = self.data["X_left"] - self.data["X_right"]
        self.result["D^2"] = np.square(self.result["D"])

        LAMBDA = 589.3 * 10**(-6)
        self.result["R_"] = self.round_dec(np.mean( np.array([
            ([self.result["D^2"][m]] - self.result["D^2"][n]) / (4*4*LAMBDA)
                for m, n in zip(range(0, 4), range(4, 8)) ])), 3)


    def write_result(self):
        """ """
        D_2 = [str(self.round_dec(n, 3)) for n in self.result["D^2"]]
        R_ = str(self.result['R_'])

        self.Ostream(f"暗环直径: {self.result['D']}\n"
                     f"暗环直径平方: {D_2}\n"
                     f"牛顿环半径: {R_}\n")

