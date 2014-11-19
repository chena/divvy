import unittest
import linkedlist as L
from linkedlist import Node

class LinkedlistTest(unittest.TestCase):

	def setUp(self):
		self.n1 = Node('a')
		self.n2 = Node('b')
		self.n3 = Node('c')
		self.n1.next = self.n2
		self.n2.next = self.n3

	def test_delete_node(self):
		head = L.delete_node(self.n1, 'b')
		self.assertEqual(head.next, self.n3)

	def test_delete_head(self):
		head = L.delete_node(self.n1, 'a')
		self.assertEqual(head.val, 'b')

	def test_delete_tail(self):
		L.delete_node(self.n1, 'c')
		self.assertEqual(self.n2.next, None)

if __name__ == '__main__':
	unittest.main()