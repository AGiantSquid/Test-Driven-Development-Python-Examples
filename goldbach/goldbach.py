import math
from collections import OrderedDict

class goldbach():
	def even_numbers(self, max):
		even_array = []
		for i in range(4, max, 2):
			even_array.append(i)
		return even_array

	def is_prime(self, num):
		if num % 1 or num < 2:
			return False
		if num % 2 == 0:
			return num == 2
		if num % 3 == 0:
			return num == 3
		sq = int (math.sqrt(num))
		for i in range(5, sq, 6):
			if num % i == 0:
				return False
			if num % ( i + 2) == 0:
				return False
		return True

	def primes_of(self, num):
		prime_array = []
		for i in range(1, num):
			if self.is_prime(i):
				y = num-i
				if y<i:
					pass
				elif self.is_prime(y):
					prime_array.append((i,y))
		return prime_array

	def goldbachs(self, max):
		goldbach_dict = OrderedDict()
		for even_number in self.even_numbers(max):
			goldbach_dict[even_number] = self.primes_of(even_number)
		return goldbach_dict

if __name__ == '__main__':
	a = goldbach()
	print(a.goldbachs(100))
