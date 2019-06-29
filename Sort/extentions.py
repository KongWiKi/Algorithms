"""
@time : 2019/6/29下午1:32
@Author: kongwiki
@File: extentions.py
@Email: kongwiki@163.com
"""
"""
与相关算法无关的函数
"""
import random
from Sort.config import *

# 随机产生整数数组
def randomList(start=GENRATE_START, stop=GENRATE_STOP, leng=GENRATE_NUM):
    """
    随机生产一个长度为50的整数数组
    :param start: 生成随机数字的开始
    :param stop: 生成随机数字的结束
    :param leng: 随机数组的长度
    :return: arrylist 随机数组
    """
    start, stop = int(start), int(stop) if start<=stop else (int(stop), int(start))
    arrayList = []
    for i in range(leng):
        arrayList.append(random.randint(start, stop))
    return arrayList