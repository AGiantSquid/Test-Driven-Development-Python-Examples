import unittest
from fibonacci import fib
class FibonacciTestSuite(unittest.TestCase):
	
	def test_fibonacci(self):
		cases=[(0, 0), (1, 1), (2, 1), (3, 2), (4, 3)]
		for i in range(0, len(cases)):
			self.assertEqual( cases[i][1], fib(cases[i][0]) )	

if __name__ == '__main__':
   unittest.main()