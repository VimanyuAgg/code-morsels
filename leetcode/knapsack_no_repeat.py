def knapsack_no_repeat(w, v, cap):
    '''
    Output the maximum value for a knapsack with capacity cap in which items can't be repeated
    :param w: weight array of items - list(int)
    :param v: value array of items - list(int)
    :param cap: max carrying capacity of knapsack
    :return: max value of the knapsack (int)
    '''
    assert len(v) == len(w), "Issue in weights & value arrays"

    if cap <= 0:
        return 0

    dp = [[0 for _ in range(cap + 1)] for __ in range(len(v) + 1)]

    for i in range(1, len(v)+1):
        for c in range(1, cap + 1):

            if w[i-1] <= c:
                # If it fits and we include the current item, does the value of knapsack of max capacity c increases?
                dp[i][c] = max(v[i-1] + dp[i-1][c - w[i - 1]], dp[i-1][c])

            else:
                # print(f"i:{i}, c:{c}")
                dp[i][c] = dp[i-1][c]

    print(*dp, sep='\n')
    return dp[len(v)][cap]
