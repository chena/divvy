import unittest
import sorting as S

class SortTest(unittest.TestCase):

	def setUp(self):
		self.lst = [4, 5, 3, 1, 2]

	def test_bubble_sort(self):
		S.bubble_sort(self.lst)
		self.assertEqual(self.lst, [1, 2, 3, 4, 5])

	def test_select_sort(self):
		S.select_sort(self.lst)
		self.assertEqual(self.lst, [1, 2, 3, 4, 5])

	def test_inset_sort(self):
		S.insert_sort(self.lst)
		self.assertEqual(self.lst, [1, 2, 3, 4, 5])

	def merge(self):
		S.merge()
		self.assertEqual(self.merge([1, 2, 3, 4], [2, 3, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
	unittest.main()

