import numpy as np
from .experiment import Experiment
from .tools import Pipe, round_dec
from functools import partial


class Newton_ring(Experiment):
    """牛顿环实验"""

    def __init__(self):
        self.data: dict = None
        self.result = {}

    def input(self, raw_data: dict):
        self.data = {key: np.array(val) for key, val in raw_data.items()}

    def process(self):
        self.result["D"] = self.data["X_left"] - self.data["X_right"]
        self.result["D^2"] = np.square(self.result["D"])

        LAMBDA = 589.3 * 10 ** (-6)
        self.result["R_"] = (
            Pipe
            | zip(self.result["D^2"][0:4], self.result["D^2"][4:8])
            | partial(map, lambda tp: (tp[0] - tp[1]) / (4 * 4 * LAMBDA))
            | np.array
            | np.mean
            | partial(round_dec, 3)
            | None
        )

    def output(self) -> str:
        D_2 = [str(round_dec(n, 3)) for n in self.result["D^2"]]
        R_ = str(self.result["R_"])

        return "暗环直径: {}\n暗环直径平方: {}\n牛顿环半径: {}\n".format(self.result["D"], D_2, R_)
