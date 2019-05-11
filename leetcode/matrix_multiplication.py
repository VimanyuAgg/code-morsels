def matrix_multiplication1(m1,m2):

    if m1 is None or m2 is None:
        return None

    if len(m1[0]) != len(m2):
        return None

    p = [[0 for _ in range(len(m2[0]))] for __ in range(len(m1))]

    # assuming m1 has dimensions (mxn) & m2 has dimensions (nxp)
    for i in range(len(m1)): # m
        for j in range(len(m2[0])): # p
            for k in range(len(m1[0])): # n
                p[i][j] = p[i][j] + m1[i][k] * m2[k][j]
    return p


def matrix_multiplication2(m1,m2):

    if m1 is None or m2 is None:
        return None

    if len(m1[0]) != len(m2):
        return None

    return [[sum(x*y for x,y in zip(m1_r,m2_c)) for m2_c in zip(*m2)] for m1_r in m1]