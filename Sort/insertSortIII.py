"""
@time : 2019/6/29下午5:34
@Author: kongwiki
@File: insertSortIII.py
@Email: kongwiki@163.com
"""
"""
使用链表来优化插入排序
"""
from Sort.extentions import randomList


def insert(arrayList, next, i):
    j = -1
    # print("当前j为{}, next[j]={}，arrayList[next[j]]={} arrayList[i]={}".format(j, next[j], arrayList[next[j]], arrayList[i]))
    while next[j] != -1 and arrayList[next[j]] < arrayList[i]:
        j = next[j]
        # print("目前j={}".format(j))
    next[j], next[i] = i, next[j]
    # print("交换后的next[j]={}, next[i]={} \n".format(next[j], next[i]))


def reorder(arrayList, next):
    i = -1
    ys = []
    while next[i] != -1:
        ys.append(arrayList[next[i]])
        i = next[i]
    return ys


def insertSortIII(arrayList):
    arrayLen = len(arrayList)
    next = [-1]*(arrayLen+1)
    for i in range(arrayLen):
        insert(arrayList, next, i)
    return reorder(arrayList, next)


if __name__ == '__main__':
    print("==========     随机生成整数数组     ==========")
    arrayList = randomList()
    print(arrayList)
    print("==========随机生成整数数组排序后的结果==========")
    arrayList = insertSortIII(arrayList)
    print(arrayList)

