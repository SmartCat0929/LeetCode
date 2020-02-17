# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 21:53
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    :
# @File    : 100. Same Tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return (p is not None and q is not None and p.val == q.val and self.isSameTree(p.left,
                                                                                       q.left) and self.isSameTree(
            p.right, q.right)) or (p is None and q is None)
