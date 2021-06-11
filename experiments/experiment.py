import os
import json
from decimal import Decimal, ROUND_HALF_UP


class Experiment():
    """所有物理实验的基类"""


    def __init__(self):
        pass


    @classmethod
    def getPrefix(cls, backward = -2, path = __file__):
        """递归获取倒数第|backward|级目录路径
        param: int backward, str path
        return: str path_head
        """
        return path if backward == 0 else cls.getPrefix(backward + 1, os.path.split(path)[0])


    def Istream(self):
        """读取指定文件的内容
        param: None
        return: str content
        """
        file = os.path.join(self.getPrefix(), 'input', self.io + ".json")
        with open(file, 'r') as fp:
            content = json.load(fp)
        return content


    def Ostream(self, content):
        """向指定文件写入内容
        param: str content
        return: None
        """
        file = os.path.join(self.getPrefix(), 'output', self.io + ".txt")
        with open(file, 'w') as fp:
            fp.write(content)


    def print_template(self):
        """显示出实验的原始数据模板
        param: None
        return: None
        """
        file = os.path.join(self.getPrefix(), 'template', self.template)
        with open(file, 'r') as fp:
            print(fp.read())


    def collect_data(self):
        """收集数据，
           成功读取输入则返回0，失败则返回-1
        param: str raw_data
        return: None
        """
        code = 0
        try:
            raw_data = self.Istream()
        except IOError:
            code = -1
        else:
            self.collect_way(raw_data)

        return code


    def collect_way(self, raw_data):
        """收集数据的方式
        param: str raw_data
        return: None
        """
        pass


    def write_result(self):
        """将数据处理结果写入文件
        param: None
        return: None
        """
        pass


    def process(self):
        """处理实验数据，或是函数的集合，或只有一个功能
        param: None
        return: None
        """
        pass


    @classmethod
    def round_dec(cls, n, d):
        """将小数n按保留位d进行四舍五入
        param: float n, int d
        return: str s
        """
        s = '0.' + '0' * d
        return float(Decimal(str(n)).quantize(Decimal(s), rounding=ROUND_HALF_UP))

