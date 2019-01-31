def suffix_arrays(string):
	return [val[1] for val in do_bwt(string)]


def do_bwt(string):
	'''Creates all substr combinations of the current string, sort them
	returns tuples of the last value of each and it's position index in string'''
	double_str = string + string
	all_combinations = [(double_str[i:i+len(string)],i) for i in range(len(string))]
	sorted_combinations = sorted(all_combinations, key=lambda k: k[0])
	result = []
	for val in sorted_combinations:
		result.append((val[0][-1],val[1]))
	return result

print(suffix_arrays('GAGAGAGA$'))