def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	# handle the empty matrix_dot_vector
	if not a or not b[0]:
		return -1 if b else []
	
	if len(a[0])!= len(b):
		return -1
	
	result = []
	for row in a:
		row_sum = sum(row[i] * b[i] for i in range(len(b)))
		result.append(row_sum)
	
	return result

	
