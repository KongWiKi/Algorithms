## 数据结构

## 二叉树

#### 定义

每个节点最多有两个子树（不存在度大于2的节点），且有左右之分，不能颠倒，其基础的形态有五中：

![](https://raw.githubusercontent.com/KongWiki/cloudImg/master/binaryTree.png)



#### 性质

* 在二叉树中，第 i层上至多有$$2^{i-1}$$个节点（i≥1）
* 深度为k的二叉树至多有$$2^k-1$$个节点（k≥1）
* 对一棵二叉树，如果叶子节点的个数为$n_0$，度为2的节点个数为$n_2$，则$n_0$ = $n_2$ + 1

* 具有n个节点的完全二叉树的深度为$$\lfloor\log_2{n}\rfloor$$ + 1

## 二叉搜索树

#### 特点

其每个节点的值大于或等于其左子树的值 小于或等于其右子树的值

**时间复杂度**：

1. 查找最小值： O(h)[h 为树的高度]\
2. 查找最大值： O(h)3 
3. 出入数据： O(h)
4. 删除数据： O(h)
5. 搜索数据： O(h)

#### 实现(递归)

```python
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
```

