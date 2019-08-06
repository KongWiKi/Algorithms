"""
@time : 2019/8/6下午9:38
@Author: kongwiki
@File: queue.py
@Email: kongwiki@163.com
"""
"""
队列：
特性：先进先出
抽象数据类型(ADT):
1. Queue() 创建一个队列 返回一个空队列
2. enqueue(item) 入队 无返回值
3. dequeue() 出队 返回队首元素 队列被修改
4. isEmpty() 查看是否为空 返回bool值
5. size() 返回队列长度
应用场景
烫手山芋： 山芋在每个人的手上传递 停止时拿到山芋的人弹出队列
"""
import random


class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		# print("当前插入的值为{}".format(item))
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def topqueue(self):
		return self.items[-1]

	def size(self):
		return len(self.items)


def hotPotato(nameList, num):
	simqueue = Queue()
	for name in nameList:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(num):
			print("弹出并入对的人{}".format(simqueue.topqueue()))
			simqueue.enqueue(simqueue.dequeue())
			print("当前队列情况为{} \n".format(simqueue.items))

	return simqueue.dequeue()


if __name__ == '__main__':
	q = Queue()
	# for i in range(5):
	# 	q.enqueue(random.randint(10, 100))
	# print("当前队列是否为空 {}".format(q.isEmpty()))
	# print("当前队列的值有 {}".format(q.items))
	# print("弹出队首元素 队首元素为{}".format(q.dequeue()))
	# print("当前队列是否为空 {}".format(q.isEmpty()))
	namelist = ['Bil', 'Weikunkun', 'Susan', 'Jane', 'Brad', 'Willam']
	print(hotPotato(namelist, 7))
