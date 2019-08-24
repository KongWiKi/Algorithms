"""
@time : 2019/8/24下午8:01
@Author: kongwiki
@File: bubbleSort.py
@Email: kongwiki@163.com
"""
from Sort.extentions import randomList


def bubbleSort(arraylist):
	"""
	冒泡排  基于交换的排序
	:param arraylist:
	:return:
	"""
	if not arraylist:
		return []
	arrayLen = len(arraylist)
	for i in range(arrayLen-1):
		for j in range(arrayLen-1-i):
			if arraylist[j] > arraylist[j+1]:
				# tmp = current
				# current = arraylist[i+1]
				# arraylist[i+1] = tmp
				arraylist[j], arraylist[j+1] = arraylist[j+1], arraylist[j]
	return arraylist

if __name__ == '__main__':
	print("==========     随机生成整数数组     ==========")
	arraylist = randomList()
	print(arraylist)
	arraylist = bubbleSort(arraylist)
	print("==========随机生成整数数组排序后结果==========")
	print(arraylist)