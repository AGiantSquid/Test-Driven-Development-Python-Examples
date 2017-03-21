import goldbach
import unittest

class goldbachTest(unittest.TestCase):
	goldbach = goldbach.goldbach()

	def test_even_numbers(self):
		self.assertEqual(self.goldbach.even_numbers(6), [4])
		self.assertEqual(self.goldbach.even_numbers(20), [4, 6, 8, 10, 12, 14, 16, 18])

	def test_is_prime(self):
		self.assertFalse(self.goldbach.is_prime(1))
		self.assertTrue(self.goldbach.is_prime(2))
		self.assertFalse(self.goldbach.is_prime(4))

	def test_primes_of(self):
		self.assertEqual(self.goldbach.primes_of(4), [(2, 2)])
		self.assertEqual(self.goldbach.primes_of(8), [(3, 5)])
		self.assertEqual(self.goldbach.primes_of(10), [(3, 7), (5, 5)])

	def test_goldbachs(self):
		self.assertEqual(self.goldbach.goldbachs(6),{4: [(2, 2)]})
		self.assertEqual(self.goldbach.goldbachs(8),{4: [(2, 2)], 6: [(3, 3)]})