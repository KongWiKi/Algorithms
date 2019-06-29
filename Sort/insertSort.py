"""
@time : 2019/6/29上午10:29
@Author: kongwiki
@File: insertSort.py
@Email: kongwiki@163.com
"""
from Sort.extentions import randomList


def insertSort(arraylist):
    """
    插入排序，因为从右向左遍历相比于从左向右移动移动次数少
    所以使用从右向左遍历已排序好的数组
    :param arraylist: 随机生成的数组
    :return: 排序好的数组（AESC）
    """
    arrayLen = len(arraylist)
    for i in range(1, arrayLen):
        current = arraylist[i]
        j = i-1
        while j >= 0 and current < arraylist[j]:
            # 后移
            arraylist[j+1] = arraylist[j]
            j = j-1
        arraylist[j+1] = current
    return arraylist


if __name__ == '__main__':
    print("==========     随机生成整数数组     ==========")
    arraylist = randomList()
    print(arraylist)
    arraylist = insertSort(arraylist)
    print("==========随机生成整数数组排序后结果==========")
    print(arraylist)