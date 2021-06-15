import numpy as np
from .experiment import Experiment

class Newton_ring(Experiment):
    """牛顿环实验"""

    def __init__(self):
        self.template = "newton_ring.txt"
        self.io = "牛顿环实验"
        self.data = None
        self.result = {}

