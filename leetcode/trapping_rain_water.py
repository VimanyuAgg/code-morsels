def trap_rain_water(arr):
    if arr is None or len(arr) <= 2:
        return 0

    l_max = find_max(arr)
    r_max = find_max(arr[::-1])[::-1]
    water = 0
    for i, val in enumerate(arr):
        if i == 0 or i == len(arr) - 1:  # not needed
            continue

        diff = abs(val - min(l_max[i],r_max[i]))
        print(f"val:{val}, l_max[i]:{l_max[i]}, r_max[i]:{r_max[i]}, diff:{diff}")
        water += diff if diff > 0 else 0
    return water

def find_max(arr):
    m = arr[0]
    res = []
    for i in arr:
        if m < i:
            m = i

        res.append(m)

    return res
