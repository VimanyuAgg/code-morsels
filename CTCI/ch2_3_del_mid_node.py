def delete_mid_node(c):
    '''C is the node to be deleted and not the head of the node'''
    if c.val is None or c.next is None:
        del c
        return
    n = c.next
    c.val = c.next.val
    c.next = n.next
    n.next = None
    del n
