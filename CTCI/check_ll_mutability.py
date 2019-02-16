from CTCI.linked_list import Node

def check1():
    n1 = Node(3)
    n2 = Node(4)
    n3 = Node(5)
    n4 = Node(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    change_list(n1)
    print("****")
    print(n1)
    print(n2)
    print(n3)
    print(n4)

def change_list(h):
    h.next = h.next.next
    h = h.next
    # h.next = h.next.next


def check2():
    h = Node(3)
    change_list2(h)
    print(h)
    print(h.next)
    print(h.next.next)
    print(h.next.next.next)

def change_list2(n):
    n1 = Node(3)
    n2 = Node(4)
    n3 = Node(5)
    n4 = Node(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n.next = n1

def check3():
    n1 = Node(300)
    n1.next = Node(400)
    n1.next.next = Node(500)
    h = n1
    h.next = Node(10000)
    print(n1)

check1()
check2()
check3()