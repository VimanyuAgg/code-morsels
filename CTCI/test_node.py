import unittest
from CTCI.linked_list import Node

class TestNode(unittest.TestCase):

    def testNullNodeCreation(self):
        h = Node()
        print(h)
        self.assertEqual(h, None)
        self.assertEqual(h.val, None)
        self.assertEqual(h.next, None)

    def testNodeCreation(self):
        h = Node(3)
        # self.assertEqual(print(h), "Node(3)->None")
        self.assertEqual(h.val, 3)
        self.assertEqual(h.next, None)

    def testNonNodeAddition(self):
        h = Node(3)
        with self.assertRaises(TypeError):
            h.next = 5

    def testListCreation(self):
        h = Node(3)
        h2 = Node(4)
        h.next = h2
        self.assertEqual(h.val, 3)
        self.assertEqual(h.next, h2)

    def testListManipulation(self):
        h = Node(3)
        h2 = Node(4)
        h3 = Node(5)
        h.next = h2
        h.next.next = h3
        self.assertEqual(h2.next, h3)
        h.next = h3
        self.assertEqual(h.next, h3)

    def testListManipulationInCallable(self):
        h = Node(3)
        h2 = Node(4)
        h3 = Node(5)
        self.__addNode(h,h2)
        self.assertEqual(h.next, h2)
        self.__addNode(h.next,h3)
        self.assertEqual(h2.next, h3)
        h.next = h3
        self.assertEqual(h.next, h3)

    def __addNode(self,n1,n2):
        n1.next = n2


if __name__ == "__main__":
    unittest.main()
