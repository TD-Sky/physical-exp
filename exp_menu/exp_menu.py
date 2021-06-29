from . import experiments as exps


class ExpMenu():
    """实验菜单"""

    def __init__(self):
        self.menu = (exps.Micrometer, 
                    exps.Vernier_caliper,
                    exps.Solar_battery,
                    exps.Pn_junction,
                    exps.E_oscilloscope,
                    exps.Newton_ring,
                    exps.Non_linear)

        self.using = None


    def choose(self, num):
        """选择实验
        param: int num
        return: None
        """
        self.using = self.menu[num]()


    def remake(self):
        """重置选择, 释放资源
        param: None
        return: None
        """
        self.using = None

