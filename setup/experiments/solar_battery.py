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
            raw_data = self.Istream('input', self.input)
        except IOError:
            return -1

        lines = [ [float(s) for s in line.split()] for line in raw_data.splitlines() if line != '' ]
        cols = list(zip(*lines))
        self.data['R'] = cols[0]
        self.data['I/mA'] = cols[1]
        self.data['U/V'] = cols[2]


    def process(self):
        """ """
        Ps = [ I*U for I, U in zip(self.data['I/mA'], self.data['U/V']) ]
        P_R = self.R_of_Pmax(Ps, self.data['R'])

        self.result['P/mW'] = [self.round_dec(P, 3) for P in Ps]
        self.result['P_R'] = P_R


    def write_result(self):
        """ """
        P_str = 'P/mW\n'
        for P in self.result['P/mW']:
            P_str += f'{self.round_dec(P, 3)}\n'
        else:
            P_str += '\n'

        self.Ostream('output', self.output,
                P_str + 
                f"最大输出功率: {self.round_dec(self.result['P_R'][0], 3)}\n" + 
                f"相应电阻值: {int(self.result['P_R'][1])}\n")


    @staticmethod
    def R_of_Pmax(Ps, Rs):
        """返回最大输出功率及其相应的电阻值
        param: list Ps, tuple Rs
        return: tuple P_R
        """
        Pmax = 0
        corespond_R = 0

        for P, R in zip(Ps, Rs):
            if Pmax < P:
                Pmax = P
            corespond_R = R

        return (Pmax, corespond_R)

