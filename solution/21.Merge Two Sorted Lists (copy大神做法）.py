# -*- coding: utf-8 -*-
# @Time    : 2020/2/1 18:30
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 21.Merge Two Sorted Lists (copy大神做法）.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        while(l1 is not None and l2 is not None):
            if l1.val <=l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
        while l1:
            l3.next = ListNode(l1.val)
            l3 = l3.next
            l1 = l1.next
        while l2:
            l3.next = ListNode(l2.val)
            l3 = l3.next
            l2 = l2.next
        return head.next

h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(4)

h2 = ListNode(1)
h2.next = ListNode(3)
h2.next.next = ListNode(4)

h = Solution().mergeTwoLists(h1, h2)
while h is not None:
    print(h.val, end="->")
    h = h.next