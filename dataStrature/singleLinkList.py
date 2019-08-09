"""
@time : 2019/8/5下午3:19
@Author: kongwiki
@File: singleLinkList.py
@Email: kongwiki@163.com
"""
"""
单链表的实现
"""


class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self, newNext):
		self.next = newNext


class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		"""
		链表插入头插法 只不过没有设置头节点
		:param item:
		:return:
		"""
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != Node and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = previous.getNext()
		else:
			previous.setNext(current.getNext())


# 有序链表
# ADT
# OrderList: 创建新的空有序链表 返回一个空的有序链表
# add(item): 在有序链表中添加元素 无返回值
# remove(item): 在有序链表中添加元素 无返回值
# search(item): 在有序链表中搜索元素 返回bool
# size(): 返回有序链表的长度
# isEmpty(): 判断是否为空 返回bool
# pop(): 弹出有序链表中最后一个项
# pop(pos): 删除并返回传入位置的元素
# index(): 返回当前值的索引
class OrderList:
	def __init__(self):
		self.head = None

	def add(self, item):
		previous = None
		current = self.head
		stop = False
		while current!=None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()
		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)


	def remove(self, item):
		pass

	def search(self, item):
		found = False
		stop = False
		current = self.head
		while current!=None and not stop and not found:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found

	def pop(self):
		pass

	def pop(self, pos):
		pass

	def isEmpty(self):
		pass

	def size(self):
		pass


if __name__ == '__main__':
	# temp = Node(5)
	# print(temp.getData())
	mylist = UnorderedList()
	mylist.add(11)
	mylist.add(15)
	mylist.add(19)
	mylist.add(100)
	mylist.add(10)
	mylist.add(89)
	mylist.add(79)
	print(mylist.search(100))
	print(mylist.size())
