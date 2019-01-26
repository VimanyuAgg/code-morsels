def min_refills_original(x,n,L):
	refill_count = 0
	loc = 1
	cur_fuel = L
	while loc < len(x)-1:
		cur_fuel -= (x[loc] - x[loc-1])
		if cur_fuel < 0:
			return "impossible"

		if cur_fuel >= x[loc+1] - x[loc]:
			pass
		else:
			refill_count += 1
			print("refilling at station:{}".format(x[loc]))
			cur_fuel = L
		loc += 1
	return refill_count
