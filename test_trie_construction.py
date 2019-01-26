import unittest
from trie_construction import Node, trie_construction, trie_matching

class NodeTests(unittest.TestCase):

    # def test_creation_1(self):
    #     node = Node()
    #     self.assertEqual(node.val, None)
    #     self.assertEqual(node.val, None)
    #
    #
    # def test_creation_2(self):
    #     n1 = Node(3)
    #     n2 = Node(4,n1)
    #     self.assertEqual(n2.next,[n1])
    #     self.assertEqual(n2.next_vals, {3})
    #
    #
    # def test_creation_3(self):
    #     n1 = Node(3)
    #     n2 = Node(4,n1)
    #     n3 = Node(10)
    #     n2.next = n3
    #     self.assertEqual(n2.next,[n1, n3])
    #     self.assertEqual(n2.next_vals, {3,10})
    # #
    # #
    # def test_is_leaf(self):
    #     node = Node(3)
    #     self.assertEqual(node.is_leaf, True)
    #
    #
    # def test_trie_constuction(self):
    #     t1 = trie_construction(["anas", 'add'])
    #     self.assertEqual(t1.next_vals,{'a'})
    #     t1_child1 = t1.next[0]
    #     self.assertEqual(t1_child1.val, 'a')
    #     self.assertEqual(t1_child1.next_vals, {'n','d'})
    #     t1_child2_1, t1_child2_2 = t1_child1.next
    #     self.assertEqual({t1_child2_1.val, t1_child2_2.val},{'n','d'})
    #     t1_child3_1 = t1_child2_1.next[0]
    #     t1_child3_2 = t1_child2_2.next[0]
    #     if t1_child3_1.val == 'd':
    #         self.assertEqual(t1_child3_1.is_leaf, True)
    #     else:
    #         self.assertEqual(t1_child3_2.is_leaf, True)

    def test_herding_patterns(self):
        trie_matching("bananas",["ananas","add"])






if __name__ == "__main__":
    unittest.main()