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