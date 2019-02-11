from CTCI.linked_list import Node

def sum_lists(head1, head2):
    l1 = head1
    l2 = head2
    sum = Node()
    print("init sum: {}".format(sum))
    carry = 0
    counter = 0

    while(l1 != None or l2 != None):

        print("iteration: {} - sum: {}, carry = {}".format(counter,sum,carry))
        counter += 1
        val = carry
        if (l1 != None):
            val += l1.val
            l1 = l1.next

        if (l2 != None):
            val += l2.val
            l2 = l2.next

        if sum.val is None:
            sum.val = val %10
            carry = val//10
        else:
            new_node = Node(val%10)
            carry = val//10
            new_node.next = sum
            sum = new_node

    if carry > 0:
        ## sum must have already been updated so it cannot be None
        new_node = Node(carry)
        new_node.next = sum
        sum = new_node

    return sum
