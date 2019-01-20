from collections import Counter
def is_anagram_original(iter1, iter2):
	return Counter(map(lambda x: x.lower(), iter1)) == Counter(map(lambda x: x.lower(),iter2))


def is_anagram_2(iter1, iter2):
	return sorted(iter1.lower()) == sorted(iter2.lower())

import re
def is_anagram_original_sanitize(iter1,iter2):
	return Counter(re.sub(r"[\s'-]+",'',iter1.lower())) == Counter(re.sub(r"[\s'-]+",'',iter2.lower()))



import unicodedata
def count_words(iterable):
	iterable = unicodedata.normalize('NFKD',iterable)
	return Counter(c for c in iterable.lower() if c.isalpha())

def is_anagram_after_1(iter1, iter2):
	return count_words(iter1) == count_words(iter2)
