"""
@time : 2019/8/9上午8:32
@Author: kongwiki
@File: binarySearch.py
@Email: kongwiki@163.com
"""


def binatySearch(arraylist, key):
	listLen = len(arraylist)
	low = 0
	high = listLen
	while low < high:
		mid = (low + high) // 2
		if key == arraylist[mid]:
			return mid
		elif key < arraylist[mid]:
			high = mid
		else:
			low = mid + 1
		# elif key > arraylist[mid]:
		# 	low = mid + 1
		# else:
		# 	high = mid
	return low


if __name__ == '__main__':
	a = [13, 16, 17, 20, 29, 60, 89]
	print(binatySearch(a, 29))