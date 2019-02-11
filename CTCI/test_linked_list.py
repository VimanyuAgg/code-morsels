from CTCI.linked_list import LinkedList
import unittest

class TestLinkedList(unittest.TestCase):

    def testLinkedListCreation(self):
        ll = LinkedList([1,2,3,4])
        print(ll)




if __name__ == "__main__":
    unittest.main()