class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

a = ListNode("A")
b = ListNode("B")
c = ListNode("C")
d = ListNode("D")
e = ListNode("E")
f = ListNode("F")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
head1 = a

q = ListNode("Q")
r = ListNode("R")
q.next = r
head2 = q

# head1: A --> B --> C --> D --> E --> F --> None
# head2: Q --> R --> None



''' Traversal - Return Values '''

def getValuesIter(head):
    curr = head
    values = []
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values
    
def getValuesRecursive(head):
    return _getValuesRecursive(head, [])
def _getValuesRecursive(node, values):
    # BASE CASE - think about the while loop condition! 
    if not node:
        return values
    values = values + [node.val]
    return  _getValuesRecursive(node.next, values)
# print(getValuesRecursive(a))




''' Node Deletion by Value '''

# iterate to the Node where value 
def delete_node(head, target):
    if head.val == target:
        return head.next

    prev = head
    curr = head.next

    while curr:
        if curr.val == target:
            prev.next = curr.next
            return head
        curr = curr.next

    return head


deletedHead = delete_node(head1, "A")
# print(getValuesIter(deletedHead))




''' Zipper Lists Redux '''

def zipperListsRedux(head1, head2):
    while head2:            # this won't work if len(h1) > len(h2)
        nxt = head1.next
        head1.next = head2
        head1 = head2
        head2 = nxt

print(f"h1: {getValuesIter(head1)}")
print(f"h2: {getValuesIter(head2)}")
zipperListsRedux(head1, head2)
print(f"combined: {getValuesIter(head1)}")






''' Zipper Lists '''

def zipperListsIter(h1, h2):
    if not h1:
        return h2

    count = 0                   # even (h2) / odd (h1) - starting h2 because we're initializing off h1

    tail = h1                   # tail is responsible for updating references to new nodes
    curr1 = h1.next             # curr1 starts at second node now that tail is initialized to the first
    curr2 = head2               # curr2 starts at beginning

    while curr1 and curr2:
        if count % 2 == 0:      # evens take from h2
            tail.next = curr2
            curr2 = curr2.next
        else:
            tail.next = curr1
            curr1 = curr1.next
        tail = tail.next
        count += 1

    if not curr1:
        tail.next = curr2
    else:
        tail.next = curr1

    return h1


def zipperListsRecursive(h1, h2):
    if not h1 and not h2:
        return None
    if not h1:
        return h2
    if not h2:
        return h1

    next1 = h1.next
    next2 = h2.next
    h1.next = h2
    h2.next = zipperListsRecursive(next1, next2)
    return h1

mergedHead = zipperListsRecursive(head1, head2)
# print(getValuesIter(mergedHead))


''' Reverse Linked List '''

def reverseLinkedListIter(node):
    prev = None
    curr = node
    while curr:
        nxt = curr.next         # set temp value / dummy head
        curr.next = prev        # update node pointer to previous node
        prev = curr             # bump prev up
        curr = nxt              # bump curr up
    return prev

# Still need to keep track of state - use default arguments
def reversedLinkedListRecursive(node, prev=None):
    if not node:
        return prev
    nxt = node.next
    node.next = prev
    return reversedLinkedListRecursive(nxt, node)
    
# nodeReversed = reversedLinkedListRecursive(a)
# print(getValuesIter(nodeReversed))




''' Get Node Value '''

def getLinkedListNode(node, index):
    curr = node
    while curr:
        if index == 0:
            return curr.val
        curr = curr.next 
        index -= 1

    if index > 0:
        return False

# print(getLinkedListNode(a, 4))




''' Linked List Find '''

def linkedListFindIter(node, target):
    curr = node
    while curr:
        if curr.val == target:
            return True
        curr = curr.next
    return False

def linkedListFindRecursive(node, target):
    if not node:
        return False
    if node.val == target:
        return True

    return linkedListFindRecursive(node.next, target)

# print(linkedListFindRecursive(a, "C"))




''' Total Sum '''

def totalSumIter(node):
    total, curr = 0, node
    while curr:
        total += curr.val
        curr = curr.next
    return total

def totalSumRecursive(node):
    return _totalSumRecursive(node, 0)
    
def _totalSumRecursive(node, total):
    if not node:
        return total
    total += node.val
    return _totalSumRecursive(node.next, total)

# print(totalSumRecursive(a))

        

