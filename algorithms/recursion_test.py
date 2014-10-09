import unittest
import recursion as R

class RecursionTest(unittest.TestCase):

	def test_stairs(self):
		self.assertEqual(R.go_up_stairs(3), 4)

if __name__ == '__main__':
	unittest.main()