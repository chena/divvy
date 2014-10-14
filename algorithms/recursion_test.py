import unittest
import recursion as R

class RecursionTest(unittest.TestCase):

	def test_stairs(self):
		self.assertEqual(R.go_up_stairs(3), 4)

	def test_make_change(self):
		self.assertEqual(R.make_change(100, [1, 5, 10, 25]), 242)

if __name__ == '__main__':
	unittest.main()