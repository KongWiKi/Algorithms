"""
@time : 2019/6/29上午10:28
@Author: kongwiki
@File: quickSort.py
@Email: kongwiki@163.com
"""
from Sort.extentions import randomList


def quickSort(arrylist):
	if not arrylist:
		return []
	pivot = arrylist[0]
	preArray = sorted(filter(lambda x: x <= pivot, arrylist[1:]))
	postArray = sorted(filter(lambda x: x >= pivot, arrylist[1:]))
	return preArray + [pivot] + postArray


if __name__ == '__main__':
	print("==========     随机生成整数数组     ==========")
	arraylist = randomList()
	print(arraylist)
	arraylist = quickSort(arraylist)
	print("==========随机生成整数数组排序后结果==========")
	print(arraylist)
