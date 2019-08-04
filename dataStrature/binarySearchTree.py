"""
@time : 2019/7/31上午9:12
@Author: kongwiki
@File: binarySearchTree.py
@Email: kongwiki@163.com
"""
"""
二叉搜索树的特点：
其每个节点的值大于或等于其左子树的值 小于或等于其右子树的值
时间复杂度：
1 查找最小值： O(h)[h 为树的高度]
2 查找最大值： O(h)
3 出入数据： O(h)
4 删除数据： O(h)
5 搜索数据： O(h)
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, newData):
        """
        插入数据
        # edage case: 若是value相同如何解决 Word天
        :param newData:
        :return:
        """
        if newData == self.data:
            return False
        elif newData < self.data:
            if self.leftChild == None:
                self.leftChild = TreeNode(newData)
            else:
                return self.leftChild.insert(newData)
        else:
            if self.rightChild == None:
                self.rightChild = TreeNode(newData)
            else:
                return self.rightChild.insert(newData)

    def findValue(self, newData):
        """
        查找值
        记得添加return 否者其无返回值 会继续的查找 却无法返回该值
        :param newData:
        :return:
        """
        if newData == self.data:
            return True
        elif newData < self.data:
            if self.leftChild:
                return self.leftChild.findValue(newData)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.findValue(newData)
            else:
                return False

    # 以下的前中后遍历均为递归的遍历
    def preOrder(self):
        """
        前序遍历
        根左右
        :return:
        """
        print(self.data)
        if self.leftChild:
            self.leftChild.preOrder()
        else:
            self.rightChild.preOrder()

    def inOrder(self):
        """
        中序遍历
        左根右
        :return:
        """
        if self.leftChild:
            self.leftChild.inOrder()
        print(self.data)
        if self.rightChild:
            self.rightChild.inOrder()

    def postOrder(self):
        """
        后序遍历
        左右根
        :return:
        """
        if self.leftChild:
            self.leftChild.postOrder()
        if self.rightChild:
            self.rightChild.postOrder()
        print(self.data)


if __name__ == '__main__':
    array = [3, 8, 9, 1, 2]
    node = TreeNode(5)
    for i in range(len(array)):
        node.insert(array[i])
    node.inOrder()
    print(node.findValue(8))