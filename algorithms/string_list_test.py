from __future__ import division
import unittest
import string_list as SL

class StringListTest(unittest.TestCase):

	def test_compress(self):
		self.assertEqual(SL.compress('aabcccccaaa'), 'a2b1c5a3')

	def test_reverse(self):
		self.assertEqual(SL.reverse('alice'), 'ecila')
		self.assertEqual(SL.reverse('abc'), 'cba')

		self.assertEqual(SL.reverse_recursive('alice'), 'ecila')
		self.assertEqual(SL.reverse_recursive('abc'), 'cba')

	def test_anagram(self):
		self.assertTrue(SL.is_anagram('alice', 'ceali'))
		self.assertFalse(SL.is_anagram('aee', 'ae'))

	def test_unique(self):
		self.assertTrue(SL.string_unique_n2('alice'))
		self.assertFalse(SL.string_unique_n('alicechen'))

	def test_remove_dupp(self):
		self.assertEqual(SL.remove_dup_naive('aab'), 'ab')
		self.assertEqual(SL.remove_dup_set('alialiaa'), 'ail')

	def test_replace_space(self):
		self.assertEqual(SL.replace_space('a b  c '), 'a%20b%20%20c%20')

	def test_rotate_mat(self):
		self.assertEqual(SL.rotate_mat([[1,2,3], [4, 5, 6]]), [(4,1), (5, 2), (6,3)])

	def test_set_zero(self):
		self.assertEqual(SL.set_mat_zero(
			[[0, 1, 2], [3, 4, 5], [6, 0, 7]]), 
			[[0, 0, 0], [0, 0, 5], [0, 0, 0]])

	def test_rotated_str(self):
		self.assertTrue(SL.check_rotated('alice', 'licea'))
		self.assertFalse(SL.check_rotated('alice', 'lice'))

	def test_most_common(self):
		self.assertEqual(SL.most_common([1, 4, 5, 5, 3, 3, 5]), 5)

	def test_largest_k(self):
		self.assertEqual(SL.largest_k_sort([4,3,1,5], 2), [4, 5])
		self.assertEqual(SL.largest_k_select([4,3,1,5], 2), [5, 4])

	def test_pair_sum(self):
		self.assertEqual(SL.find_sum_pair([1, 2, 3, 4], 5), [(1, 4), (2, 3)])

	def test_palindrome(self):
		self.assertTrue(SL.check_palindrome('racecar'))
		self.assertFalse(SL.check_palindrome('alice'))

	def test_best_profit(self):
		self.assertEqual(SL.best_profit([2, 5, 3, 1, 6]), 5)

	def test_find_unique(self):
		self.assertEqual(SL.find_unique([1, 2, 2]), 1)
		self.assertEqual(SL.find_unique([2, 1, 2]), 1)
		self.assertEqual(SL.find_unique([2, 2, 1]), 1)

	def test_find_single(self):
		self.assertEqual(SL.find_unique([1, 3, 2, 3, 2]), 1)
		self.assertEqual(SL.find_unique([2, 1, 3, 2, 3]), 1)
		self.assertEqual(SL.find_unique([3, 3, 2, 2, 1]), 1)

	def test_find_products(self):
		self.assertEqual(SL.find_products([1, 2, 5, 3]), [30, 15, 6, 10])
		self.assertEqual(SL.find_products_no_div([1, 2, 5, 3]), [30, 15, 6, 10])

	def test_shuffle(self):
		arr = [1, 2, 3, 4, 5]
		SL.shuffle_array(arr)
		self.assertNotEqual(arr, [1, 2, 3, 4, 5])

if __name__ == '__main__':
	unittest.main()
