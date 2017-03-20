import unittest
from evenFibonacciNumbers import fibonacci_numbers
class EvenFibonacciTestSuite(unittest.TestCase):
	
	def test_even_fibonaccis(self):
		cases=[(0, 0), (2, 2), (8, 10)]
		for i in range(0, len(cases)):
			self.assertEqual( cases[i][1], fibonacci_numbers(cases[i][0]) )	

if __name__ == '__main__':
   unittest.main()