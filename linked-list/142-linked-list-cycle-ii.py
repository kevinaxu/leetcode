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

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # print(f"slow: {slow.val}, fast: {fast.val}")
            if slow == fast:
                return True
        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        the key intuition here is that when fast and slow meet
        we reset slow back to head
        then we move them until they collide again
        this will happen at the entry point fo the loop so we return either
        '''
        slow = fast = head
        # is_second_pass = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # print(f"slow: {slow.val}, fast: {fast.val}")
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow 
        return None



a = ListNode("A")
b = ListNode("B")
c = ListNode("C")
d = ListNode("D")
a.next = b
b.next = c
c.next = d
d.next = b      # introduce cycle
head = a

# A --> B --> A --> None
# Solution().print_list(head)
print(Solution().detectCycle(head).val)
# Solution().print_list(newList)

