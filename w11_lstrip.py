def lstrip_original(iterable, key):
	flag = False
	if isinstance(key,int) or isinstance(key, str):
		for val in iterable:
			if (not flag):
				if val == key:
					continue
				else:
					yield val
					flag = True

			else:
				yield val

	else:
		for val in iterable:
			if (not flag):
				if key(val):
					continue
				else:
					yield val
					flag = True

			else:
				yield val

from itertools import dropwhile
def lstrip_after(iterable, key):
	return dropwhile(lambda x: x==key, iterable)

def lstrip_after_2(iterable,key):
	if callable(key):
		return dropwhile(key, iterable)
	else:
		return dropwhile(lambda x: x ==key, iterable)

def lstrip_after_3(iterable, key):
	iterator = iter(iterable)
	for val in iterator:
		if (callable(key) and (not key(val))) or ((not callable(key)) and val != key):
			yield val
			break
	yield from iterator
