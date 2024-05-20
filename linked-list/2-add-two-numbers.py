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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1, curr2 = l1, l2 
        carry, digit = 0, 0 

        dummy = ListNode()
        tail = dummy

        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            total = v1 + v2 + carry 
            digit = total % 10
            carry = total // 10 

            node = ListNode(digit)
            tail.next = node
            tail = node

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        return dummy.next 




a = ListNode(9)
b = ListNode(9)
# c = ListNode(9)
# d = ListNode(9)
a.next = b
# b.next = c
# d.next = d
l1 = a

q = ListNode(9)
# r = ListNode(9)
# s = ListNode(9)
# q.next = r
# r.next = s
l2 = q

head = Solution().addTwoNumbers(l1, l2)
Solution().printList(head)








'''
LC solution (ChatGPT) 
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    dummyHead = ListNode(0)
    tail = dummyHead
    carry = 0

    while l1 or l2 or carry != 0:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0 

        total = v1 + v2 + carry
        digit = total % 10
        carry = total // 10

        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    result = dummyHead.next             # smart...we don't even use originaly dummyHead. It's just a placeholder
    return dummyHead.next
'''


'''
Original Attempt
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    curr1, curr2 = l1, l2
    total = 0
    shouldCarry = False

    result, tail = None, None

    while curr1 and curr2:
        print("derr")
        v1 = curr1.val if curr1 else 0
        v2 = curr2.val if curr2 else 0
        total = v1 + v2

        print(f"total: {total}")
        if shouldCarry:
            total += 1
            shouldCarry = False
        if total >= 10:
            total -= 10
            shouldCarry = True

        newNode = ListNode(total, None)
        if not result:
            result = newNode
            tail = result
        else:
            tail.next = newNode
            tail = tail.next

        curr1 = curr1.next
        curr2 = curr2.next

    if not curr1 and not curr2:
        return result

    if not curr1:
        total = curr2.val 
        if shouldCarry: total += 1
        if total >= 10: total -= 10
        curr2.val = total 
        curr2.next.val = 1
        tail.next = curr2
    else:
        total = curr1.val 
        if shouldCarry: total += 1
        if total >= 10: total -= 10
        curr1.val = total 
        curr1.next.val = 1
        tail.next = curr1

    return result
'''
    