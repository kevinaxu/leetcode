class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedListDouble:

    def __init__(self):
        self.num_nodes = 0
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        '''
        if empty linked list, add the node and update tail / head dummy nodes 
        '''
        newNode = ListNode(value)
        if self.num_nodes == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.num_nodes += 1

    def add_to_head(self, value):
        newNode = ListNode(value)
        if self.num_nodes == 0:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.num_nodes += 1

    def remove_from_tail(self):
        if self.num_nodes == 0:
            return -1

        self.num_nodes -= 1
        tail_val = self.tail.val
        if self.num_nodes == 0:     # check if we still have nodes in the ll 
            self.tail = self.head = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return tail_val


    def remove_from_head(self):
        if self.num_nodes == 0:
            return -1

        self.num_nodes -= 1
        head_val = self.head.val
        if self.num_nodes == 0:     # check if we still have nodes in the ll 
            self.tail = self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return head_val

    def remove_by_value(self, value):
        '''
        3 scenarios: head / tail / middle
        '''
        if self.num_nodes == 0:
            return -1

        if self.head.val == value:
            return self.remove_from_head()
        elif self.tail.val == value:
            return self.remove_from_tail()
        else:
            curr = self.head.next
            while curr:
                if curr.val == value:                   # delete node from middle 
                    curr.prev = curr.next
                    curr.next = curr.prev 
                    self.num_nodes -= 1
                    return curr.val
                curr = curr.next
            return -1 
            
    def get_values(self):
        curr = self.head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

    def print(self):
        values = ' <--> '.join(self.get_values())
        print(f"nodes: {self.num_nodes}, values: {values}")


ll = LinkedListDouble()
ll.add_to_tail("B")
ll.add_to_tail("C")
ll.add_to_head("A")
ll.print()
print(f"removing: {ll.remove_from_head()}")
print(f"removing: {ll.remove_by_value('A')}")


ll.print()