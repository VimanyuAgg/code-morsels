def urlify(s):
    '''
    Converts the spaces in string s to %20. There's buffer at the end
    :param s: str
    :return: str
    '''
    # Assumes that there are enough white spaces at the end or we'd need to a pass to verify if there's enough space
    if not s:
        return s

    l = list(s)
    p1 = len(s)-1
    p2 = len(s)-1

    while l[p1] == " ":
        p1 -= 1

    while p1 > 0:
        if l[p1] != " ":
            l[p2] = l[p1]
            p2 -= 1
            p1 -= 1

        else:
            p1 -= 1
            l[p2-2:p2+1] = "%20"
            p2 -= 3
            # l[p2] = "0"
            # l[p2-1] = "2"
            # l[p2-2] = "%"
            # p2 -= 3

    # There might be more white spaces than we need
    return ''.join(l[p2:])


