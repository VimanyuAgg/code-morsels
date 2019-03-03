import itertools

def combinations(iterable, r):
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	#r=2
	# combinations(range(4), 3) --> 012 013 023 123
	pool = tuple(iterable)
	#'a'.'b','c','d'
	print("pool: {}".format(pool))
	n = len(pool)
	#n=4
	print("n: {}".format(n))
	if r > n:
		return
	indices = list(range(r))
	# 0,1
	print("indices: {}".format(indices))
	print ("yielding: tuple(pool[i] for i in indices): {}".format(tuple(pool[i] for i in indices)))
	#'a','b'
	yield tuple(pool[i] for i in indices)
	while True:
		print("reversed(range(r)): {}".format(list(reversed(range(r)))))
		#[1,0]
		for i in reversed(range(r)):
			print("i: {}".format(i))
			#i=1
			#i=0
			print("checking if indices[{}] != {} + {} - {}".format(i,i,n,r))
			#for i=1
			#chek-1:1!=1+4-2
			#check-1:1!=3
			#check-2: 2!=1+4-2
			#check-2: 2!=3
			#check-3: 3!=1+4-2
			#check-2: 3!=3 (not true print not successful, go to zero)

			#for i=0
			#check-1: 0!=0+4-2
			#check1: 0!=2



			if indices[i] != i + n - r:
				print("check successful")
				break

			print("check NOT successful")
			#now going for i=0

			if (i==0):


				print("for loop runs complete")

		else:
			print ("**** RETURNING ****")
			return
		print("*after for* indice[{}] incremented from {} to {}".format(i,indices[i],indices[i]+1))
		#check-1: indice1 from 1 to 2
		#check-2: indice1 from 2 to 3
		#for i=0
		#check-1 : indice0 from 0to 1

		indices[i] += 1
		#check-1: indice[i]=2
		#check-2: indice[i]=3
		# for i=0
		# check-1 : indice[0]=1

		print("looping through j in range({},{})".format(i+1,r))
		#check-1:(2,2)
		#check-2:(2,2)
		# for i=0, j will run
		# check-1 : (1,2)
		for j in range(i+1, r):
			print("current j: {}".format(j))
			# j=1
			indices[j] = indices[j-1] + 1

			print("indices[{}] = indices[{}] + 1".format(j,j-1))
			#indices[1]= indices[0]+1
			#indices[1]= 2

			print("new indices j: {}".format(indices[j]))
			#new indices[j]=2
		else:
			print("*** end of j *****")

		print("yielding tuple(pool[i] for i in indices): {}".format(tuple(pool[i] for i in indices)))
		#check-1: 'a'.'b'
		#check-2: 'a','c'

		#for i=0,
			#indices[0]=1
		    #indices[j]=2

		yield tuple(pool[i] for i in indices)
		print("***end***")


combination_string = combinations('ABCD', 2)
print(list(combination_string))






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
