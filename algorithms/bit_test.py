from __future__ import division
import unittest
import bit as B

class BitTest(unittest.TestCase):

	def test_to_binary(self):
		self.assertEqual(B.to_binary('25.75'), '11001.11')

if __name__ == '__main__':
	unittest.main()