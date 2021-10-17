# 自定义工具包
import os
from decimal import Decimal, ROUND_HALF_UP


class PipeMeta(type):
    """元类"""
    def __or__(cls, obj):
        return cls(obj)


class Pipe(metaclass=PipeMeta):
    """管道组合宏
    e.g: Pipe | val | fn1 | fn2 | None
    等价于: fn2(fn1(val))
    """

    def __init__(self, obj):
        self._obj = obj

    def __or__(self, fn):
        if callable(fn):
            return type(self)(fn(self._obj))
        elif fn is None:
            return self._obj
        else:
            return NotImplemented


def getPrefix(path: str, backward: int = 0) -> str:
    """获取绝对路径的倒数第|backward|级绝对路径; 位置[0]表示末路径"""
    return path if backward == 0 \
        else getPrefix(os.path.split(path)[0], backward + 1)


def round_dec(n: float, d: int) -> Decimal:
    """将小数n按保留位d进行四舍五入"""
    s = '0.' + '0' * d
    return Decimal(str(n)).quantize(Decimal(s), rounding=ROUND_HALF_UP)
