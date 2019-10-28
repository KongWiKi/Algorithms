"""
@time : 2019/9/16上午10:40
@Author: kongwiki
@File: tree.py
@Email: kongwiki@163.com
"""
"""
树的各种存储
"""


# 列表表示
# myTree = ['a', ['b', ['d', [], []], ['e', [], []] ], ['c', ['f', [], []], []] ]
# print(myTree)
# print("left subtree=", myTree[1])
# print("root = ", myTree[0])
# print("right subtree= ", myTree[2])


def BinatyTree(r):
	return [r, [], []]


def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root
