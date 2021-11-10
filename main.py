import sys
import toml
from experiments import *

if __name__ == "__main__":

    # 数据输入模块
    in_data_file = sys.argv[1]
    in_data = None
    with open(in_data_file) as fp:
        in_data = toml.load(fp)

    # 数据处理模块
    exp_name = in_data["name"]
    exps = {
        "solar_battery": Solar_battery,
        "e_oscilloscope": E_oscilloscope,
        "micrometer": Micrometer,
        "newton_ring": Newton_ring,
        "pn_junction": Pn_junction,
        "vernier_caliper": Vernier_caliper,
        "young_modulus": Young_modulus,
    }
    exp = exps[exp_name]()
    exp.input(in_data)
    exp.process()

    # 数据输出模块
    exp.draw()
    out_data = exp.output()
    sys.stdout.write(out_data)
