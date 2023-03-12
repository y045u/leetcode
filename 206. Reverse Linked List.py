# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        res = None
        while head:
            curr = head # 向きを反転させるターゲットのノード
            head = head.next
            curr.next = res # ターゲットのノードの向きをresへ向ける
            res = curr
        return res
