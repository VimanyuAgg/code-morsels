from collections import defaultdict

def group_by_original(iterable, key_func=lambda x: x):
	result_dict = defaultdict(list)
	for val in iterable:
		result_dict[key_func(val)].append(val)
	return result_dict


from itertools import groupby
def group_by_itertools(iterable,key_func=lambda x:x):
	iterable = sorted(iterable, key = key_func)
	return {
		key: list(val)
		for key, val in groupby(iterable, key = key_func)
    }
