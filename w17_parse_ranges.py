
def parse_ranges_after_2(string_val):
	for group in string_val.split(","):
		start, sep, end = group.partition("-")
		if end and not end.startswith(">"):
			yield from range(int(start), int(end)+1)
		else:
			yield int(start)

def partition(sep, val):
	begin,sep, end = val.partition(sep)
	return (begin, begin) if (not sep) or end.startswith(">") else (begin, end)

def parse_ranges_after(string_val):
	pairs = (
        partition("-", val)
        for val in string_val.split(",")
        )
	return (num
            for low, high in pairs
            for num in range(int(low), int(high)+1)
            )


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


