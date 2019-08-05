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

    def __str__(self):
        """
        用于输出调试
        :return:
        """
        return "<Node: value>: {}, next={}>".format(self.data, self.next)

    __repr__ = __str__


class LinkList(object):
    """
    链表ADT
    [hNode] ---> [Node0] ---> [Node1]
    """
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.root = Node()
        self.tailNode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, data):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkList is Full')
        node = Node(data)
        tailNode = self.tailNode
        if tailNode is None:
            self.root.next = node



