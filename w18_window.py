def window_original(seq, n):
    if n == 0 or seq is None or len(seq) < n:
        return []

    i = n
    res = []
    while i < len(seq)+1:
        res.append(tuple(seq[j] for j in range(i-n, i)))
        i += 1

    return res

def window_1(seq,n):
    if n == 0 or seq is None or len(seq) < n:
        return []

    res = []
    i = n

    while i < len(seq)+1:
        res.append(tuple(seq[i-n:i]))
        i+=1

    return res




