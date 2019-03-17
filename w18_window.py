from collections import deque
def window_original(seq, n):
    if n == 0 or seq is None or len(seq) < n:
        return []

    i = n
    res = []
    while i < len(seq)+1:
        res.append(tuple(seq[j] for j in range(i-n, i)))
        i += 1

    return res


def window_1(seq, n):
    if n == 0 or seq is None or len(seq) < n:
        return []

    res = []
    i = n

    while i < len(seq)+1:
        res.append(tuple(seq[i-n:i]))
        i += 1

    return res


def window_2(seq, n):
    if n == 0 or seq is None or len(seq) < n:
        return []

    sequences = [seq[i:] for i in range(n)]

    return zip(*sequences)


def window_3(seq, n):
    res = []
    entry = []

    for s in seq:
        if len(entry) < n:
            entry.append(s)
            continue

        res.append(tuple(entry))

        entry.append(s)
        entry = entry[1:]

    res.append(tuple(entry))
    return res


def window_4(seq, n):
    entry = []

    for s in seq:
        if len(entry) < n:
            entry.append(s)
            continue

        yield tuple(entry)

        entry.append(s)
        entry = entry[1:]

    yield tuple(entry)



if __name__ == "__main__":
    inputs = (n**2 for n in [1, 2, 3, 4, 5])
    iterable = window_4(inputs, 2)
    print(iter(iterable))
    print(iter(iterable))
    print(iter(iterable) == iter(iterable))
    print(next(iterable))