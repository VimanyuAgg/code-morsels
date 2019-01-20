def multimax_original(iterable):
	iterable = list(iterable)
	return [x for x in iterable if x == max(iterable)]

def basic(arg):
	return arg

def multimax_original_iterable(iterable, key = basic):
	result = []
	flag = True
	for i in iterable:
		if flag or key(i) > key(result[0]):
			if len(result) > 0:
				result = list()
			result.append(i)
			flag = False
		elif key(i) == key(result[0]):
			result.append(i)
	return result

def multimax_after(iterable, key = lambda x: x):
	# PEP8 discourages when lambda is assigned to be a variable
	maximums = []
	for i in iterable:
		if not maximums or key(i) == key(maximums[0]):
			maximums.append(i)
		elif key(i) > key(maximums[0]):
			maximums = [i]
	return maximums
