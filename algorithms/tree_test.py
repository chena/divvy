import unittest
import tree as T
from tree import Node

class TreeTest(unittest.TestCase):

	def setUp(self):
		self.n4 = Node(4)
		n3 = Node(3)
		n6 = Node(6)
		n7 = Node(7)

		n2 = Node(2, self.n4, n3)
		n5 = Node(5, n6, n7)
		self.n1 = Node(1, n2, n5)

		n2.parent = self.n1
		n5.parent = self.n1
		self.n4.parent = n2
		n3.parent = n2
		n6.parent = n5
		n7.parent = n5

	def test_sum_paths(self):
		self.assertEqual(T.sum_paths(self.n1, 6), [[1, 2, 3], [2, 4], [1, 5], [6]])

	def test_preorder(self):
		self.assertEqual(T.preorder(self.n1, []), [1, 2, 4, 3, 5, 6, 7])

	def test_levelorder(self):
		self.assertEqual(T.levelorder(self.n1), [[1], [2,5], [4,3,6,7]])

	def test_balanced(self):
		self.assertTrue(T.check_balance(self.n1))

	def test_inorder(self):
		self.assertEqual(T.inorder(self.n1), [4, 2, 3, 1, 6, 5, 7])

	def test_sum(self):
		self.assertEqual(T.sum_tree(self.n1), 28)

	def test_to_tree(self):
		tree = T.to_tree([4, 2, 5, 1, 6, 3, 7], 0, 6)
		self.assertEqual(T.levelorder(tree), [[1], [2, 3], [4, 5, 6, 7]])

if __name__ == '__main__':
	unittest.main()