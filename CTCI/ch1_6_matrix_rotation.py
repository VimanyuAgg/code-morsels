def rotate_90(m):
    if not m or (len(m) == 0):
        return False

    n = len(m)
    for i in range(0, n):
        if len(m) != len(m[i]):
            return False

    for layer in range(0, len(m) // 2):
        last = n - 1 - layer
        for i in range(layer, last):
            temp = m[layer][i]
            m[layer][i] = m[n - 1 - i][layer]
            m[n - 1 - i][layer] = m[last][n - 1 - i]
            m[last][n - 1 - i] = m[i][last]
            m[i][last] = temp

    return True


def rotate_90_not_inplace(m):
    if not m or (len(m) == 0):
        return False

    n = len(m)
    for i in range(0, n):
        if len(m) != len(m[i]):
            return False

    m = m[::-1]
    return list(map(list, zip(*m)))