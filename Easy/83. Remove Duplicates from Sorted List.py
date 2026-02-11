# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next if cur.next.next else cur.next
            cur = cur.next
        return head