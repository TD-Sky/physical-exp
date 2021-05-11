import pprint
from .experiment import Experiment


class Solar_battery(Experiment):
    """太阳能电池基本特性的测量"""

    def __init__(self):
        self.template = "solar_battery.txt"
        self.input = "太阳能电池基本特性的测量.txt"
        self.output = "太阳能电池基本特性的测量.txt"
        self.data = {}
        self.result = {}
    

    def collect_data(self):
        """ """
        try:
            raw_data = self.Istream(self.input)
        except IOError:
            return -1

        lines = [ [float(s) for s in line.split()] for line in raw_data.splitlines() if line != '' ]
        cols = list(zip(*lines))
        self.data['R'], self.data['I/mA'], self.data['U/V'] = cols[0], cols[1], cols[2]


    def process(self):
        """ """
        Ps = [ I*U for I, U in zip(self.data['I/mA'], self.data['U/V']) ]

        self.result['P/mW'] = [self.round_dec(P, 3) for P in Ps]



