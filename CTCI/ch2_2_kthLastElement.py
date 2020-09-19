class Node:
    next = None

    def __init__(self, val):
        self.val = val

# 1th last element == last element
def kthFromLast(head, k):
    if head is None or (k <= 0):
        return None

    current = head
    runner = head

    # check for off-by-1
    for i in range(0, k - 1):
        if runner is None:
            return -1

        runner = runner.next

    while runner.next is not None:
        current = current.next
        runner = runner.next

    return current.val


def create_ll():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    return n1


n1 = create_ll()
print(kthFromLast(n1, 10))