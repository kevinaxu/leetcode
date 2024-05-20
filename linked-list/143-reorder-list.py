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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev

    def zipperList(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        tail = head1
        curr1 = head1.next      # starting with h1
        curr2 = head2 

        count = 0
        while curr1 and curr2:
            if count % 2 == 0:  # pull from h2
                tail.next = curr2
                curr2 = curr2.next
            else:
                tail.next = curr1
                curr1 = curr1.next
            tail = tail.next
            count += 1

        if not curr1:
            tail.next = curr2
        if not curr2:
            tail.next = curr1
        return head1


    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Step 1: Find the middle of the list - use slow / fast iterators
        Step 2: Reverse the second part of the linked list
        Step 3: Zipper list 
        '''
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if not slow.next:           # handle len(ll) = 1 
            return head

        ''' Step 2: Reverse the second part of the linked list '''
        head2 = self.reverseList(slow.next)
        slow.next = None            # split the two lists 
        # self.printList(head)
        # self.printList(head2)

        ''' Step 3: Zipper list '''
        head = self.zipperList(head, head2)
        # print("combined:")
        # self.printList(head)



# A -> B -> None
# s    f   
        

a = ListNode("A")
# b = ListNode("B")
# c = ListNode("C")
# d = ListNode("D")
# e = ListNode("E")
# f = ListNode("F")
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
head1 = a

Solution().reorderList(head1)