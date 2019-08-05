"""
@time : 2019/8/5下午7:16
@Author: kongwiki
@File: doubleLinkList.py
@Email: kongwiki@163.com
"""
"""
双向链表
"""


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.pre = self.next = None
