# 2. Add Two Numbers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    carry = 0
    curr = dummy_head
    while (l1 != None or l2 != None):
        if l1 == None:
            x = 0
        else:
            x = l1.val
            l1 = l1.next

        if l2 == None:
            y = 0
        else:
            y = l2.val
            l2 = l2.next
        num_sum = x + y + carry

        carry = num_sum // 10
        curr.next = ListNode(num_sum % 10)
        curr = curr.next

    if carry > 0:
        curr.next = ListNode(carry)

    return dummy_head.next


l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)
m1.next = m2
m2.next = m3


addTwoNumbers(l1, m1)