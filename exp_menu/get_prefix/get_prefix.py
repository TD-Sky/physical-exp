import os

def getPrefix(path: str, backward: int = 0) -> str:
    """获取绝对路径的倒数第|backward|级绝对路径; 位置[0]表示末路径
    param: int backward, str path
    return: str path_prefix
    """
    return path if backward == 0 \
                else getPrefix(os.path.split(path)[0], backward + 1)


if __name__ == "__main__":
    print("当前文件: ", getPrefix(__file__))
    print("倒数第1级: ", getPrefix(__file__, -1))
    print("倒数第3级: ", getPrefix(__file__, -3))

