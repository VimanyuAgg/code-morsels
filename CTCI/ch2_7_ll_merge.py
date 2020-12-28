

class Node:
    next = None

    def __init__(self, val):
        self.val = val


def get_ll_length_and_last_node(l):
    if (not l):
        return 0

    if l.next is None:
        return 1

    length = 0

    while l.next:
        length += 1
        l = l.next

    return length, l


def list_by_length(l1, l2):
    counter1, last1 = get_ll_length_and_last_node(l1)
    counter2, last2 = get_ll_length_and_last_node(l2)

    if counter1 > counter2:
        return l2, l1, last1 is last2
    else:
        return l1, l2, last1 is last2


def find_ll_merge_point(l1, l2):
    if (not l1) or (not l2):
        return None

    len1, last1 = get_ll_length_and_last_node(l1)
    len2, last2 = get_ll_length_and_last_node(l2)

    if last1 is last2:
        # Link Lists merge at some point
        smaller_ll, larger_ll, len_sm, len_lg = (l1, l2, len1, len2) if len1 < len2 else (l2, l1, len2, len1)
        return find_ll_intersection_helper(smaller_ll, larger_ll, len_sm, len_lg)
    else:
        return None


def find_ll_intersection_helper(sm, lg, len_sm, len_lg):
    len_diff = len_lg - len_sm
    for i in range(0, len_diff):
        lg = lg.next

    while sm.next is not None:
        if sm is lg:
            return sm
        sm = sm.next
        lg = lg.next
    return sm


def create_ll():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n2_1 = Node(2)
    n4_1 = Node(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n2_1.next = n4_1
    n4_1.next = n1

    return n1, n2_1


h1, h2 = create_ll()

merge = find_ll_merge_point(h1, h2)
if merge:
    print(merge.val)
else:
    print('no merge')