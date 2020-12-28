class Node:
    next = None

    def __init__(self, val):
        self.val = val


def get_length(l):
    runner = l
    counter = 0

    while runner.next:
        runner = runner.next
        counter += 1

    return counter


def pad_list(l, amount):
    for i in range(0, amount):
        print("being called for {}".format(l.val))
        n = Node(0)
        n.next = l
        l = n
    return l


def pad_lists_if_needed(l1, l2):
    length_l1 = get_length(l1)
    length_l2 = get_length(l2)

    if length_l1 < length_l2:
        l1 = pad_list(l1, length_l2 - length_l1)
    else:
        l2 = pad_list(l2, length_l1 - length_l2)

    return l1, l2


def sum_helper(head1, head2, sum, carry=0):
    if (not head1) and (not head2):
        return None, 0

    if ((not head1) and head2) or ((not head2) and head1):
        raise Exception("Padding isn't working properly")

    if (head1.next is None) and (head2.next is None):
        val = head1.val + head2.val
        sum.val = val % 10
        carry = val // 10
        return sum, carry

    if (head1.next is None and (head2.next is not None)) or (head2.next is None and (head1.next is not None)):
        raise Exception("Padding isn't working properly")

    sum, carry = sum_helper(head1.next, head2.next, sum, carry)
    n = Node(carry)
    val = head1.val + head2.val + n.val
    n.val = val % 10
    carry = val // 10
    n.next = sum
    sum = n
    return sum, carry


def sum_lists_followup(head1, head2):
    if not head1:
        return head2

    if not head2:
        return head1

    sum = Node(None)
    print("init sum: {}".format(sum))
    head1, head2 = pad_lists_if_needed(head1, head2)
    print(f"head1.val: {head1.val}")
    print(f"head2.val: {head2.val}")
    sum, carry = sum_helper(head1, head2, sum)
    if carry:
        n = Node(carry)
        n.next = sum
        sum = n
    return sum


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
r = sum_lists_followup(l1, l2)
print(r.val)
print(r.next.val)
print(r.next.next.val)
print(r.next.next.next.val)

l3 = create_ll([7, 2, 3])
l4 = create_ll([9, 9])
r2 = sum_lists_followup(l3, l4)
print(r2.val)
print(r2.next.val)
print(r2.next.next.val)