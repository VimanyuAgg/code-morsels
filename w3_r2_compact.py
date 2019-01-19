def compact(seq):
	my_iter = iter(seq)
	current_val  = next(my_iter)
	yield current_val
	while True:
		try:
			next_val = next(my_iter)
		except StopIteration as e:
			return
		if next_val == current_val:
			continue
		else:
			yield next_val
			current_val = next_val

val = compact([1,2,3])
while True:
	try:
		print(next(val))
	except StopIteration as e:
		print("That's all folks!")
		break


def compact_zip_sol(seq):
	unduped = []
	for item, prev in zip(seq, [object(), *seq]):
		if item != prev:
			unduped.append(item)
	return unduped

def compact_sol_iter(seq):
	## Consumes the lazy iterators instead of consuming when asked
	seq = list(seq)
	for i, item in enumerate(seq):
		if i == 0 or item != seq[i-1]:
			yield item

from itertools import groupby

def compact_final(seq):
	return (item for item, group in groupby(seq))

def compact_final_mysol(seq):
	it = iter(seq)
	counter = 0
	prev = next(it)
	print("init: {}".format(counter))
	yield prev
	for item in it:
		print("counter:{}".format(counter))
		counter += 1
		if item != prev:
			yield item
			prev = item
