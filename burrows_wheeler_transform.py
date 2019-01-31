def do_bwt(string):
	'''Creates all substr combinations of the current string, sort them and find the last value of each'''
	double_str = string + string
	all_combinations = [double_str[i:i+len(string)] for i in range(len(string))]
	sorted_combinations = sorted(all_combinations)
	result = ""
	for val in sorted_combinations:
		result += val[-1]
	return result


def do_inverse_bwt(bwt):
	'''Recreates the original str given the BWT'''
	original_str = "$"
	counter = 0
	index_char = [(i,val) for i,val in enumerate(bwt)]
	print(f"index_char: {index_char}")
	sorted_li = sorted(index_char, key= lambda k: k[1])
	print(f"sorted li: {sorted_li}")
	while len(original_str) < len(bwt):
		original_str += bwt[counter]
		counter = sorted_li.index((counter, bwt[counter]))

	return original_str[::-1]


# print(do_bwt("AGACATA$"))
# print(do_inverse_bwt(do_bwt("AGACATA$")))
#
# print(do_inverse_bwt('AGGGAA$'))

