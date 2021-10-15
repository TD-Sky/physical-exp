class Experiment():
    """所有物理实验的基类"""

    def __init__(self):
        pass

    def input(self, raw_data: dict):
        """加工传入的原始数据"""
        pass

    def process(self):
        """处理实验数据，或是函数的集合，或只有一个功能"""
        pass

    def draw(self):
        """绘制实验数据图"""
        pass

    def output(self) -> str:
        """返回最终结果的字符串"""
        pass
