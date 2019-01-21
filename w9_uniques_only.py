def uniques_only_original(iterable):
	result_list = []
	for val in iterable:
		if val not in result_list:
			result_list.append(val)
			yield val

li = [1,2,3]
dict.fromkeys(li)

from collections.abc import Hashable

def uniques_only_after(iterable):
	got_hashable = set()
	got_unhashable = []
	for val in iterable:
		if isinstance(val,Hashable):
			if val not in got_hashable:
				yield val
				got_hashable.add(val)
		else:
			if val not in got_unhashable:
				yield val
				got_unhashable.append(val)