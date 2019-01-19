def add_bonus(*iterable):
	iterable = list(iterable)
	result = iterable[0]
	for i in range(1, len(iterable)):
		# run as time times input iterables/matrices are given
		to_add_list = iterable[i]
		result = add_1(result, to_add_list)
	return result


def add_1(iter1, iter2):
	result = []

	if (len(iter1) != len(iter2)):
		raise ValueError("Given matrices are not the same size.")
	for i in range(0, len(iter1)):
		entry = []
		list1 = iter1[i]
		list2 = iter2[i]
		if (len(list1) != len(list2)):
			raise ValueError("Given matrices are not the same size.")
		for j in range(0, len(list1)):
			entry.append(list1[j] + list2[j])

		result.append(entry)


	return result


def add_explicit_two_only(matrix1,matrix2):
	result = []
	for r,n in zip(matrix1,matrix2):
		row = []
		for val1, val2 in zip(r,n):
			row.append(val1+val2)
		result.append(row)
	return result


def add_explicit_multiple(*matrices):
	result = []
	for rows in zip(*matrices):
		row = []
		print(rows)
		for values in zip(*rows):
			print(values)
			row.append(sum(values))
		result.append(row)
	return result

def add_after_comprehension(*matrices):
	return [
		[sum(values) for values in zip(*rows)]
		for rows in zip(*matrices)
	]


def add_after_with_exceptions(matrix1, matrix2):
	# just two input matrices
	if ([len(rows) for rows in matrix1] != [len(rows) for rows in matrix2]):
		raise ValueError("Given Matrices are of different sizes")
	return [
		[sum(val) for val in zip(*rows)]
		for rows in zip(matrix1,matrix2)
	]

def get_matrix_shape(matrix):
	return [len(row) for row in matrix]

def add_after_multiple_with_exceptions_1(*matrices):
	input_shape = get_matrix_shape(matrices[0])
	if any(get_matrix_shape(m) != input_shape for m in matrices):
		raise ValueError("Matrices given are of different length")
	return[
		[sum(values) for values in zip(*rows)]
		for rows in zip(*matrices)
]


def add_after_multiple_with_exceptions_2(*matrices):
		input_shape_set = {
			tuple(len(r) for r in m)
			for m in matrices
		}
		print(list(input_shape_set))


		print(len(list(input_shape_set)))
		if len(list(input_shape_set)) > 1:
			raise ValueError("Given Matrices aren't same in size")
		return [
			[sum(vals) for vals in zip(*rows)]
		for rows in zip(*matrices)
		]
