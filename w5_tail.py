def tail_original(seq, num):
	if num< 0:
		return []
	input_index = len(seq) - num
	print("input index is: {}".format(input_index))
	result = []
	for i in range(len(seq)):
		if i >= input_index:
			print("match found at i: {} seq[i]: {}".format(i,seq[i]))
			result.append(seq[i])

	return result


def tail_original_comprehension(seq, num):
	if num < 0:
		return []
	input_index = len(seq) - num
	return [
		seq[i]
		for i in range(len(seq))
		if i >= input_index
	]

from queue import Queue
def tail_original_iterator(seq,num):
	if num <=0:
		return []
	q = Queue(maxsize=num)
	for val in seq:
		if not q.full():
			q.put(val)
		else:
			q.get()
			q.put(val)
	result = []
	while not q.empty():
		result.append(q.get())
	return result


