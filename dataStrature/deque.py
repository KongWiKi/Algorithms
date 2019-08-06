"""
@time : 2019/8/6下午10:14
@Author: kongwiki
@File: deque.py
@Email: kongwiki@163.com
"""
"""
双端队列
性质：有两个端部 首部和尾部 可在首部和尾部天剑和删除元素
无强制的FIFO或者LIFO要求
应用：
回文字符检测
抽象数据类型(ADT):
1. Deque() 创建空的双端队列 并返回一个空的双端队列
2. addFront(item) 在首部添加元素 不返回值
3. addRear(item) 在尾部添加元素 不返回值
4. removeFront() 在首部移除元素 不返回值
5. removeRear() 在尾部移除元素 不返回值
6. isEmpty() 判断是否为空 返回bool值
7. size()  判断大小 返回双端队列的长度
"""


class Deque:
	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.insert(-1, item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		self.items.pop()

	def removeRear(self):
		self.items.pop(0)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)


if __name__ == '__main__':
	dq = Deque()
	print("双端队列是否为空 {}".format(dq.isEmpty()))
	dq.addFront(4)
	dq.addRear('dog')
	dq.addFront(5)
	dq.addRear('cat')
	print("双端队列当前的元素{}".format(dq.items))
	dq.removeFront()
	dq.removeRear()
	print("双端队列当前的元素{}".format(dq.items))