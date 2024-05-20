from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def printList(self, head: 'Optional[Node]') -> None:
        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        print(values)

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        headCopy = Node(head.val, None)
        currCopy = headCopy

        curr = head
        while curr and curr.next:
            curr = curr.next

            nodeCopy = Node(curr.val, None)
            currCopy.next = nodeCopy
            currCopy = currCopy.next

        return headCopy


a = Node(1)
b = Node(3)
c = Node(5)
# d = Node("D")
# e = Node("E")
a.next = b
b.next = c
# c.next = d
# d.next = e
head1 = a

copy = Solution().copyRandomList(head1)
Solution().printList(copy)


'''
Trick:
3 passes
1) 

'''