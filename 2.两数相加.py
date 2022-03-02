#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1: 
                v1 = l1.val
                l1 = l1.next
            if l2: 
                v2 = l2.val
                l2 = l2.next
            s = v1 + v2 + carry
            s, carry = s % 10, s // 10
            p = ListNode(s)
            cur.next = p
            cur = cur.next
        return root.next
# @lc code=end

