import unittest
from CTCI.ch2_5_sum_lists import sum_lists
from CTCI.linked_list import Node,LinkedList

class TestSumLists(unittest.TestCase):

    def test1(self):
        ll1 = LinkedList([7,1,6])
        ll2 = LinkedList([5,9, 2])
        h1 = ll1.head
        h2 = ll2.head
        sum = sum_lists(h1,h2)
        sum2 = sum
        while(sum != None):
            print(sum)
            sum = sum.next

        self.assertEqual(str(sum2),"Node(9)->Node(1)")
        self.assertEqual(str(sum2.next), "Node(1)->Node(2)")
        self.assertEqual(str(sum2.next.next), "Node(2)->None")

    def test2(self):
        ll1 = LinkedList([7,1])
        ll2 = LinkedList([5,9, 2])
        h1 = ll1.head
        h2 = ll2.head
        sum = sum_lists(h1,h2)
        sum2 = sum
        while(sum != None):
            print(sum)
            sum = sum.next

        self.assertEqual(str(sum2),"Node(3)->Node(1)")
        self.assertEqual(str(sum2.next), "Node(1)->Node(2)")
        self.assertEqual(str(sum2.next.next), "Node(2)->None")

if __name__== "__main__":
    unittest.main()