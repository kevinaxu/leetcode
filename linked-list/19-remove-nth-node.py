from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def printList(self, head: Optional[ListNode]) -> None:
        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        print(values)

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



        # if not head.next:
        #     return head.next

        # count = 0
        # slow, fast = head, head
        
        # while fast.next:
        #     fast = fast.next
        #     count += 1
        #     if count > n:
        #         prev = slow
        #         slow = slow.next
        # print(prev, slow, fast, count)
        # if count < n:           # no nth node in ll 
        #     return None

        # # prev points at previous head
        # prev.next = slow.next
        # return head

# A --> None                    n = 1, output = pointer to None?   
# s/f                                   count = 0

a = ListNode("A")
b = ListNode("B")
# c = ListNode("C")
# d = ListNode("D")
# e = ListNode("E")
a.next = b
# b.next = c
# c.next = d
# d.next = e
head1 = a

Solution().printList(head1)
Solution().removeNthFromEnd(head1, 2)
Solution().printList(head1)


