from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def _reverse(head, prev=None):
            if not head:
                return prev
            nxt = head.next
            head.next = prev
            return _reverse(nxt, head)
        return _reverse(head)

def getValuesIter(head):
    curr = head
    values = []
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values
