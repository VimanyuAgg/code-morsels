
class Node:
    next = None

    def __init__(self, val):
        self.val = val


def sum_lists(l1, l2):
    sum = Node(None)
    dummy_head = sum
    print("init sum: {}".format(sum))
    carry = 0
    counter = 0

    while (l1 != None or l2 != None):

        print("iteration: {} - sum: {}, carry = {}".format(counter, sum.val, carry))
        counter += 1
        val = carry
        if (l1 != None):
            val += l1.val
            l1 = l1.next

        if (l2 != None):
            val += l2.val
            l2 = l2.next

        new_node = Node(val % 10)
        carry = val // 10
        sum.next = new_node
        sum = new_node

    if carry:
        new_node = Node(carry)
        sum.next = new_node

    return dummy_head.next


def create_ll(item_list):
    temp = None
    head = None
    for item in item_list:
        n1 = Node(item)
        if temp:
            temp.next = n1
        if not head:
            head = n1
        temp = n1
    return head


l1 = create_ll([7, 2, 3])
l2 = create_ll([8, 2, 9])
r = sum_lists(l1, l2)
print('running through sum')
while r:
    print(r.val)
    r = r.next
