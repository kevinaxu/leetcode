from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        if list1.val <= list2.val:          # starting list is the one with the smaller val 
            head = list1
            tail = list1
            curr1 = list1.next
            curr2 = list2  
        else: 
            head = list2
            tail = list2
            curr1 = list1
            curr2 = list2.next  

        while curr1 and curr2:
                                                    # determine whether to pull from list1 or list2 
            if curr1.val > curr2.val:                # pull from curr2 
                tail.next = curr2
                tail = curr2 
                curr2 = curr2.next 
            else:
                tail.next = curr1      
                tail = curr1 
                curr1 = curr1.next 

        if not curr1:
            tail.next = curr2
        if not curr2:
            tail.next = curr1

        return head





a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
a.next = b
b.next = c
head1 = []

q = ListNode(0)
# r = ListNode(5)
# q.next = r
head2 = q

def getValuesIter(head):
    curr = head
    values = []
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values

merged = Solution().mergeTwoLists(head1, head2)
print(getValuesIter(merged))