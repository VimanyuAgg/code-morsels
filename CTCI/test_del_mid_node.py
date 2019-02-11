import unittest
from CTCI.ch2_3_del_mid_node import delete_mid_node
from CTCI.linked_list import Node, LinkedList

class TestDeleteMidNode(unittest.TestCase):

    # def test1(self):
    #     ll = LinkedList([1,2,3,4,5])
    #     c = ll.head.next.next.next
    #     print(c) #Node(4)
    #     print(ll)
    #     delete_mid_node(c)
    #     print(ll)
    #     self.assertEqual(str(ll),"Node(1)->Node(2)->Node(3)->Node(5)")

    def test2(self):
        ll = LinkedList([1,2,3,4,5])
        c = ll.head.next.next.next.next
        print(c) #Node(5)
        print(ll)
        delete_mid_node(c)
        print(ll)
        self.assertEqual(str(ll),"Node(1)->Node(2)->Node(3)->Node(4)")


if __name__=="__main__":
    unittest.main()