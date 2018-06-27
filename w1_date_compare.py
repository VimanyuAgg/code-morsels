def get_earliest(d1,d2):
    d1_arr = d1.split('/')
    d2_arr = d2.split('/')
    iteration = [2,0,1]
    for x in iteration:
        print("compare {} & {}".format(d1_arr[x], d2_arr[x]))
        if int(d1_arr[x]) == int(d2_arr[x]):
            continue
        if int(d1_arr[x]) < int(d2_arr[x]):
            return d1
        else:
            return d2

    # both dates are same
    return d1

print(get_earliest('01/27/1832','01/27/1756'))
