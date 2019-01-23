def interleave_original(seq1, seq2):
	res = []
	for i, val in enumerate(seq1):
		res.append(val)
		res.append(seq2[i])
	return res

def interleave_original_2(seq1, seq2):
	for i, val in enumerate(seq1):
		yield val
		yield seq2[i]

def interleave_original_3(seq1, seq2):
	for val in zip(seq1, seq2):
		yield val[0]
		yield val[1]


from itertools import chain
def interleave_after(seq1, seq2):
	return chain.from_iterable(zip(seq1,seq2))

def iterleave_after_2(seq1, seq2):
	return (
		val
		for pair in zip(seq1, seq2)
		for val in pair
    )