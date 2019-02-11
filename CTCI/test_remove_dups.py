import unittest
from CTCI.ch2_1_remove_dups import remove_dups
from CTCI.linked_list import Node, LinkedList


class TestRemoveDups(unittest.TestCase):

    def test1(self):
        ll = LinkedList([1,2,3,4])
        r = ll.head
        remove_dups(r)

        self.assertEqual(r.val,1)
        self.assertEqual(r.next.val, 2)
        self.assertEqual(r.next.next.val, 3)
        self.assertEqual(r.next.next.next.val, 4)

    def test2(self):
        ll = LinkedList([1, 1, 2, 3,2,1])
        r = ll.head
        remove_dups(r)

        self.assertEqual(r.val, 1)
        self.assertEqual(r.next.val, 2)
        self.assertEqual(r.next.next.val, 3)
        self.assertEqual(r.next.next.next, None)


if __name__ == "__main__":
    unittest.main()