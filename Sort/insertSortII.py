"""
@time : 2019/6/29下午1:29
@Author: kongwiki
@File: insertSortII.py
@Email: kongwiki@163.com
"""
"""
插入排序的优化I --- 折半插入
因为插入排序必须要维持一个有序的数组，然后之后的数据一次插入
所以可以使用折半查找需要插入的位置，之后从插入位置从左向右移动即可
"""
from Sort.extentions import randomList


def binarySearch(arrayList, key):
    arrayLen = len(arrayList)
    low = 0
    high = arrayLen
    while low < high:
        mid = (low + high) // 2
        if arrayList[mid] == key:
            return mid
        elif arrayList[mid] < key:
            low = mid+1
        else:
            high = mid

    return low


def insertSortII(arrayList):
    arrayLen = len(arrayList)
    for i in range(1, arrayLen):
        current = arrayList[i]
        position = binarySearch(arrayList[:i], current)
        # print("当前搜索到的位置为{}当前的数字为{}".format(position, arrayList[i]))
        for j in range(i, position, -1):
            # 后移一位
            arrayList[j] = arrayList[j-1]
        arrayList[position] = current
        # print("当前循环的结果为{}\n".format(arrayList))
    return arrayList


if __name__ == '__main__':
    print("==========     随机生成整数数组     ==========")
    arrayList = randomList()
    print(arrayList)
    print("==========随机生成整数数组排序后的结果==========")
    arrayList = insertSortII(arrayList)
    print(arrayList)