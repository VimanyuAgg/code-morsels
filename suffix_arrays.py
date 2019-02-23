def suffix_arrays(string):
	return [val[1] for val in do_bwt(string)]


def do_bwt(string):
	'''Creates all substr combinations of the current string, sort them
	returns tuples of the last value of each and it's position index in string'''
	double_str = string + string
	all_combinations = [(double_str[i:i+len(string)],i) for i in range(len(string))]
	print("all_combinations")
	print(all_combinations)
	sorted_combinations = sorted(all_combinations, key=lambda k: k[0])
	print(sorted_combinations)
	# return sorted_combinations
	result = []
	for val in sorted_combinations:
		result.append((val[0][0],val[1]))
	return result

# print(suffix_arrays('GAGAGAGAT$'))
print(suffix_arrays('ababaa$'))

def pattern_matching_suffix_arrays(text, pattern):
	suffix_arr = do_bwt(text)
	min_index = 0
	max_index = len(text)-1
	print(suffix_arr)
	while min_index < max_index:
		mid_index = (min_index+max_index)//2
		print(f"min_index:{min_index}, mid_index:{mid_index}, max_index:{max_index}")
		print(f"checking: {pattern} > {suffix_arr[mid_index][0]}- {pattern > suffix_arr[mid_index][0]}")
		if pattern > suffix_arr[mid_index][0]:
			min_index = mid_index + 1
		else:
			max_index = mid_index

	start = suffix_arr[min_index][1]
	max_index = len(text)-1
	print(start)
	print("*********")
	while min_index < max_index:
		mid_index = (min_index + max_index)//2
		print(f"min_index:{min_index}, mid_index:{mid_index}, max_index:{max_index}")
		print(f"checking: {pattern} < {suffix_arr[mid_index][0]}- {pattern < suffix_arr[mid_index][0]}")
		if pattern < suffix_arr[mid_index][0]:
			max_index = mid_index

		else:
			min_index = mid_index + 1

	end = suffix_arr[max_index][1]

	if start > end:
		return "Pattern does not exist"
	else:
		return(start,end)

# print(pattern_matching_suffix_arrays('GAGAGAGAT$', 'AG'))