from decimal import Decimal, ROUND_HALF_UP


class Experiment():
    """所有物理实验的基类"""


    def __init__(self):
        pass


    def set_path(self, DirFileName):
        """获取所需文件的绝对路径
        param: str DirFileName
        return: str path
        """
        path = '/'.join(__file__.split('/')[:-2] + [DirFileName])
        return path


    def Istream(self, suffix):
        """读取指定文件suffix的内容
        param: str suffix
        return: str content
        """
        file = self.set_path(suffix)
        with open(file, 'r') as fp:
            content = fp.read()
        return content 


    def Ostream(self, suffix, content):
        """向指定文件suffix写入内容
        param: str suffix, str content
        return: None
        """
        file = self.set_path(suffix)
        with open(file, 'w') as fp:
            fp.write(content)


    def print_template(self):
        """显示出实验的原始数据模板
        param: None
        return: None
        """
        try:
            template = self.Istream(self.template)
        except IOError:
            return -1

        print(template)


    def collect_data(self):
        """收集数据
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
        return Decimal(str(n)).quantize(Decimal(s), rounding=ROUND_HALF_UP)


