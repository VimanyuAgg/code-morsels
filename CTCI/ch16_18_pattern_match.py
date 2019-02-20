

from collections import Counter

def pattern_match(pattern, value):
    if len(value) == 0:
        return len(pattern) == 0

    if len(pattern) == 0:
        return False

    if len(pattern) == 1:
        return True

    if len(pattern) == 2 and pattern[0] != pattern[1]:
        return len(value) >= 2

    pattern_dict = dict(Counter(pattern))
    p1 = pattern[0]
    num_p1 = pattern_dict[p1]
    p2 = 'a' if p1 is 'b' else 'b' ## Pattern can consist only of a & b
    num_p2 = pattern_dict.get(p2,-1) ## it might not exist in pattern
    has_p2 = True
    if num_p2 is -1:
        has_p2 = False

    index_p2_pattern = pattern.find(p2) ## might be -1

    print(f"num_p1: {num_p1}, num_p2:{num_p2}, has_p2:{has_p2}, p2: {p2}, p1: {p1}")
    for end_p1 in range(1,len(value)):

        val_p1 = value[:end_p1]
        print(f"** end_p1: {end_p1}, val_p1: {val_p1}")
        size_p1 = num_p1*len(val_p1) ## length of all p1 inside value
        size_p2 = len(value) - size_p1
        print(f"len(value) - size_p1: {len(value)} - {size_p1}= {len(value) - size_p1}")
        if has_p2:
            len_p2 = size_p2//num_p2 # actual length of p2 element
        else:
            len_p2 = 0
        if has_p2 and len_p2 == 0:
            continue ## If b exists in pattern, it cannot be ""

        print(f"size_p1:{size_p1}, size_p2:{size_p2}, len_p2:{len_p2}")
        if size_p2 % num_p2 != 0:
            continue #len_p2 should be an integer

        offset = len(val_p1)*index_p2_pattern
        val_p2 = value[offset:len_p2+offset] if has_p2 else ""
        print(f"val_p2:{val_p2}")
        candidate = recreate_value_from_pattern(pattern,val_p1,val_p2)
        print(f"candidate: {candidate}")
        if candidate == value:
            return True
    return False

def recreate_value_from_pattern(pattern,val_p1,val_p2):
    p1 = pattern[0]
    res = ""
    for p in pattern:
        if p is p1:
            res+=val_p1
        else:
            res += val_p2
    return res
