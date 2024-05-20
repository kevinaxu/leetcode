from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def print_list(self, head: Optional[ListNode]) -> None:
        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        print(values)


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slow and fast pointers
        # fast pointer goes out n 
        # let's try this with a dummy head - does this help us with bounds checks? 
        dummy = ListNode(0)
        slow = fast = dummy.next = head 

        # move the fast head up 
        for _ in range(n):
            fast = fast.next 

        # move both pointers until fast is at the end of the ll 
        while fast:
            dummy = dummy.next
            slow = slow.next
            fast = fast.next

        # remove node 
        if slow == head:
            head = head.next
        else:
            dummy.next = slow.next
        return head 


a = ListNode("A")
b = ListNode("B")
c = ListNode("A")
# d = ListNode("D")
# e = ListNode("E")
# a.next = b
# b.next = c
# c.next = d
# d.next = e
head1 = a

# A --> B --> A --> None
Solution().print_list(head1)
newList = Solution().removeNthFromEnd(head1, 1)
Solution().print_list(newList)






'''
# neetcode solution 
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow, fast = head, head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    return head
'''