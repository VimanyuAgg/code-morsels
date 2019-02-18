n1 = (n**2 for n in range(1,5))
n2 = (n**3 for n in range(1,3))
n3 = (n**4 for n in range(1,3))

li = [n1,n2,n3]

def interleave_iterators(li):
    try:
        for it in zip(*li):
            for val in it:
                try:
                    yield val
                except StopIteration as e:
                    continue

    except StopIteration as e:
        yield -1

def interleave_after_2(seq):
    list_of_iterators = seq
    res = []
    while list_of_iterators:
        for it in list(list_of_iterators):
            try:
                yield next(it)
                # res.append(next(it))
            except StopIteration as e:
                list_of_iterators.remove(it)

    # return res


# val = interleave_iterators(li)
val2 = interleave_after_2(li)

print(val2)