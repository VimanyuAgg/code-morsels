from collections import Counter
from collections import defaultdict

#
# def count_words_m1(input_str):
# 	input_str = input_str.lower()
# 	input_arr = input_str.split(" ")
# 	for input in input_arr:
#
# 		if not input[0].isalpha():
# 			input_arr[input_arr.index(input)] = input[1:]
#
#
# 		if not input[-1].isalpha():
# 			input_arr[input_arr.index(input)] = input[:-1]
#
# 	return dict(Counter(input_arr))
#
#
# def count_words_m2(input_str):
# 	word_dict = {}
# 	input_arr = input_str.split()
# 	for word in input_arr:
# 		word = word.lower()
# 		if not word[-1].isalpha():
# 			word = word[:-1]
#
# 		if not word[0].isalpha():
# 			word = word[1:]
#
# 		if word_dict.get(word) != None:
# 			word_dict[word] += 1
# 		else:
# 			word_dict[word] = 1
#
# 	return word_dict


# def count_words_m3(input_str):
# 	print("method 3")
# 	word_dict = defaultdict(int)
# 	input_arr = input_str.split()
# 	for word in input_arr:
# 		word = word.lower()
# 		if not word[0].isalpha():
# 			word = word[1:]
# 		if not word[-1].isalpha():
# 			word = word[:-1]
#
# 		word_dict[word] += 1
#
#
# 	return word_dict

## AFTER

from collections import Counter
import re
def count_words_m1(input_str):
	return Counter(re.findall(r"\b[\w'-]+\b", input_str.lower()))


def count_words_m2(input_str):
	word_dict = defaultdict(int)
	for word in input_str.lower().split():
		word = re.findall(r"\b[\w'-]+\b", word)
		print(word[0])
		print(type(word))
		word_dict[word[0]] += 1

	return dict(word_dict)


def count_words_m3(input_str):
	word_dict = {}
	for word in input_str.lower().split():
		word = re.findall(r"\b[\w'-]+\b", word)[0]  # re.findall returns a list of strings

		word_dict[word] = word_dict.get(word, 0) + 1
	return word_dict
