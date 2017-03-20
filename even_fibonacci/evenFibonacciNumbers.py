def fibonacci_numbers(maximum):
	fibonacci_array=0
	a=0
	b=1
	c=a+b
	while maximum>=c:
		a=b
		b=c
		c=a+b
		if c%2==0 and c<= maximum:
			fibonacci_array+=c				
	return fibonacci_array

if __name__ == '__main__':
   print fibonacci_numbers(4000000)