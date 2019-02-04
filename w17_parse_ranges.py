def parse_ranges_original_3(string_val):
	iterable = string_val.split(",")
	for entry in iterable:
		if entry.find("->") != -1:
			yield int(entry.split("->")[0])
			continue

		if len(entry.split("-")) == 1:
			yield int(entry)
			continue

		low, high = entry.split("-")
		low = int(low)
		high = int(high)
		for i in range(low,high+1):
			yield i


def parse_ranges_original_2(string_val):
	iterable = string_val.split(",")
	for entry in iterable:
		if len(entry.split("-")) == 1:
			yield int(entry)
			continue
		low, high = entry.split("-")
		low = int(low)
		high = int(high)
		for i in range(low, high + 1):
			yield i

def parse_ranges_original(string_val):
	result = []
	if len(string_val) == 0:
		return []
	iterable = string_val.split(",")
	for entry in iterable:
		if len(entry.split("-")) == 1:
			result.append(int(entry))
			continue
		low, high = entry.split("-")
		low = int(low)
		high = int(high)
		for i in range(low,high+1):
			result.append(i)
	return result


