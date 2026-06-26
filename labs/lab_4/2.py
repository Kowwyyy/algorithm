# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        curr = head
        save = 0

        while l1 or l2 or save:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + save
            save = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head.next