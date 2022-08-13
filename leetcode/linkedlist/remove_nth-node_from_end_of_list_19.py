# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) -> Optional[ListNode]:
        curr = head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        if len(res) == 1:
            return []
        else:
            return res[:-n].append(res[-1])