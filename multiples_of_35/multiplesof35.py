def multiple_finder(n):
	result_array = []
	for i in range(1, n+1):
		if i%3==0 or i%5==0:
			result_array.append(i)
	return result_array