from CTCI.linked_list import Node

def remove_dups(ll_root):
    all_vals = set()
    curr = ll_root
    # if curr.val != None:
    #     all_vals.add(curr.val)
    # else:
    #     return

    all_vals.add(curr.val)

    while(curr.next != None):
        if (curr.next.val in all_vals):
            n = curr.next
            curr.next = curr.next.next
            n.next = None
            del n
        else:
            all_vals.add(curr.next.val)
            curr = curr.next