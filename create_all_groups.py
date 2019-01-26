import itertools

def combinations(iterable, r):
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# combinations(range(4), 3) --> 012 013 023 123
	pool = tuple(iterable)
	print("pool: {}".format(pool))
	n = len(pool)
	print("n: {}".format(n))
	if r > n:
		return
	indices = list(range(r))
	print("indices: {}".format(indices))
	print ("yielding: tuple(pool[i] for i in indices): {}".format(tuple(pool[i] for i in indices)))
	yield tuple(pool[i] for i in indices)
	while True:
		print("reversed(range(r)): {}".format(list(reversed(range(r)))))
		for i in reversed(range(r)):
			print("i: {}".format(i))
			print("checking if indices[{}] != {} + {} - {}".format(i,i,n,r))
			if indices[i] != i + n - r:
				print("check successful")
				break
		else:
			return
		print("indice[{}] incremented from {} to {}".format(i,indices[i],indices[i]+1))
		indices[i] += 1
		print("looping through j in range({},{})".format(i+1,r))
		for j in range(i+1, r):
			print("current j: {}".format(j))
			indices[j] = indices[j-1] + 1
			print("indices[{}] = indices[{}] + 1".format(j,j-1))
			print("new indices j: {}".format(indices[j]))
		print("yielding tuple(pool[i] for i in indices): {}".format(tuple(pool[i] for i in indices)))
		yield tuple(pool[i] for i in indices)


def group_n_after(C,n):
	return itertools.combinations(C, n)
#
# def group_n_original(C,n):
# 	if len(C) == 0 or n == 0:
# 		return []
# 	res = []
# 	for val in C:
# 		entry_group = []
# 		for i in range(1,len(C)):
# 			g = group_n_original(C[1:],n-1)
# 			if len(g) > 0:
# 				g.append(val)
# 				entry_group.append(g)
# 			else:
# 				entry_group.append(val)
#
# 		res.append(entry_group)
# 	return res
