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


    def print_template(self):
        """显示出实验的原始数据模板
        param: None
        return: None
        """
        file = self.set_path(self.template)
        with open(file, 'r') as fp:
            content = fp.read()
        print(content)


    def read_data(self):
        """读取原始数据，并储存到相应的数据结构中
        param: None
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


