from collections import deque
import itertools

def window_original(seq, n):
    if n == 0 or seq is None or len(seq) < n:
        return []

    i = n
    res = []
    while i < len(seq) + 1:
        res.append(tuple(seq[j] for j in range(i - n, i)))
        i += 1

    return res


def window_1(seq, n):
    if n == 0 or seq is None or len(seq) < n:
        return []

    res = []
    i = n

    while i < len(seq) + 1:
        res.append(tuple(seq[i - n:i]))
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
    entry = []  # works as well
    entry = deque(maxlen=n)

    #  Fails on self.assertEqual(next(inputs), 9) in lazy_iterator return

    for s in seq:
        if len(entry) < n:
            entry.append(s)
            continue

        yield tuple(entry)

        entry.append(s)
        # entry = entry[1:]

    yield tuple(entry)


def window_5(seq, n):
    entry = deque(maxlen=n)

    for s in seq:
        if len(entry) < n:
            entry.append(s)
            if len(entry) == n:
                yield tuple(entry)

            continue

        entry.append(s)
        yield tuple(entry)


def window_6(seq, n):
    entry = deque(maxlen=n)
    iterablez = iter(seq)

    for _ in range(n):
        entry.append(next(iterablez))

    yield tuple(entry)

    for n in iterablez:
        entry.append(n)
        yield tuple(entry)


def window_7(seq, n):
    iterablez = iter(seq)
    entry = deque(itertools.islice(iterablez, n), maxlen=n)
    yield tuple(entry)
    for item in iterablez:
        entry.append(item)
        yield tuple(entry)


if __name__ == "__main__":
    inputs = (n ** 2 for n in [1, 2, 3, 4, 5])
    iterable = window_4(inputs, 2)
    res1 = iter(iterable)
    res2 = iter(iterable)
    print(res1 == res2)
    print(res1 is res2)
    print(next(iterable))
