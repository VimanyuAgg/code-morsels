def interleave_original(*seq):
    return (v for pair in zip(*seq) for v in pair)

def interleave_after(*seq):
    list_of_iterators = [iter(i) for i in seq]
    while list_of_iterators:
        for it in list(list_of_iterators):
            try:
                yield next(it)
            except StopIteration as e:
                list_of_iterators.remove(it)

