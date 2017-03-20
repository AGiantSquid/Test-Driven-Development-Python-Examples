import unittest
from multiplesof35 import multiple_finder
class MultiplesTestSuite(unittest.TestCase):
	def test_multiples(self):
		self.assertEqual(multiple_finder(5), [3, 5])
		self.assertEqual(multiple_finder(30), [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30])

if __name__ == '__main__':
   unittest.main()