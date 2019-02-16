from CTCI.linked_list import Node

def intersection():
    n = Node(0)
    s = set()
    s.add(n)
    n1 = Node(0)

    if n in s:
        print("hi<-- gets printed")
    else:
        print("nay")

    if n1 in s:
        print("hi")
    else:
        print("nay <-- gets printed")


intersection()