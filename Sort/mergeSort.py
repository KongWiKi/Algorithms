"""
@time : 2019/7/21下午12:29
@Author: kongwiki
@File: mergeSort.py
@Email: kongwiki@163.com
"""
"""
原地归并排序
归并排序在所有的情况下都保证O(nlgn)的性能
且归并排序为外部排序 所以其特别适用于空间上链接的场景 
可以对非连续存储空间的序列进行排序
其本质是 分治思想
其保证划分的严格 每次都将排序序列从中间位置分割开来
然后递归的对子序列进行排序
1. 自然归并排序
2. 自底向上的归并排序
"""
from Sort.extentions import randomList


# def mergeSort(low, high, mid, arrayList):
#     """
#     归并排序最简单实现方式
#     :param low: 数组最小索引
#     :param high: 数组最大索引
#     :param mid: 中间值
#     :param arrayList: 随机生成的数组
#     :return: 排序成功数组
#     """
#     i = low
#     j = mid + 1
#     # 拷贝一份原数组 所有操作均在拷贝数组中进行
#     aux = arrayList
#
#     for k in range(low, high):
#         if (i > mid):
#             arrayList[k] = aux[j]
#             j += 1
#         elif (j > high):
#             arrayList[k] = aux[i]
#             i += 1
#         elif (aux[j] < aux[i]):
#             arrayList[k] = aux[j]
#             j += 1
#         else:
#             arrayList[k] = aux[i]
#             i += 1
#     return arrayList


def mergeSort(arraylist):
    arrayLen = len(arraylist)
    if arrayLen > 1:
        al = [x for x in arraylist[:arrayLen // 2]]
        bl = [x for x in arraylist[arrayLen // 2:]]
        al = mergeSort(al)
        bl = mergeSort(bl)
        arraylist = merge(arraylist, al, bl)
    return arraylist


def merge(arraylist, prelist, postlist):
    """
    use for merge list
    :param arraylist: 数组
    :param prelist: 原数组被切分的前一部分
    :param postlist: 原数组被切分的后一部分
    :return: 整合之后的数组
    """
    i = 0
    while prelist != [] and postlist != []:
        arraylist[i] = prelist.pop(0) if prelist[0] < postlist[0] else postlist.pop(0)
        i = i + 1

    arraylist[i:] = prelist if prelist != [] else postlist
    return arraylist


if __name__ == '__main__':
    print("==========     随机生成整数数组     ==========")
    arraylist = randomList()
    print(arraylist)
    arraylist = mergeSort(arraylist)
    print("==========随机生成整数数组排序后结果==========")
    print(arraylist)
