def deep_add_original(iterable, start=0):
	if isinstance(iterable, (int,float,complex)):
		return iterable
	if (len(iterable) == 0):
		return 0


	# for val in iterable:
	#	yield deep_copy_original(val)

	result = start
	for val in iterable:
		result += deep_add_original(val)

	return result


from collections.abc import Iterable
def deep_add_after(iterable, start = 0):
	if isinstance(iterable, Iterable):
		return sum((deep_add_after(x) for x in iterable), start)
	else:
		return iterable