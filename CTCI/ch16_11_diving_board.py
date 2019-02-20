def all_lengths_diving_board(k,shorter,longer):
    res = set()
    for i in range(k+1):
        res.add((k-i)*shorter + i*longer)

    return list(res)