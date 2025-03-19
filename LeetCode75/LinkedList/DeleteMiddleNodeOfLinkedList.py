# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Count nodes
        length, ptr = 1, head
        while ptr.next is not None:
            length += 1
            ptr = ptr.next

        # - Edge case: Size = 1
        if length == 1:
            return None

        # Find middle
        mid = int(length / 2)

        # Link pre-middle to post-middle
        i, j, ctr = head, head.next, 1
        while ctr < mid:
            i = i.next
            j = j.next
            ctr += 1
        i.next = j.next

        return head
