# 获取项目绝对路径
import os

def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == '__main__':
    print("测试路径正确性,路径为:", get_Path())