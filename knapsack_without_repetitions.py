import copy

def knapsack_without_repetitions_recursive(capacity, w_arr, val_arr):
    ## Recursive implementation

    print("called")
    ## Base case
    if len(val_arr) == 0 or capacity == 0:
        return 0


    w_v_zip = list(zip(w_arr,val_arr)) # need to do sanitization that both have same size, no neg values and capacity is positive as well

    print(f"w_v_zip:{w_v_zip}")
    max_value = 0
    for i in range(len(w_arr)):

        if w_v_zip[i][0] > capacity:
            continue

        #OUTER_CASE1: w_arr[i] might be in the solution

            ##Case1: It is in solution but not in solution for capacity - w_arr[i]
            ## In this case we simply add it to solution for capacity - w_arr[i]
            ## i.e. answer = w_v_zip[i][1]+ knapsack_without_repetition(capacity - w_arr[i],w_arr.remove(w_v_zip[i][0]), v_arr.remove(w_v_zip[i][0]))

            ##Case2: It is in solution but also in solution for capacity - w_arr[i]
            ## In this case what we get is optimal solution for capacity - w_arr[i] in which w_arr doesn't contain ith item

            #In both cases, we reduce the problem to a knapsack of smaller weight with reduced number of items
        w_arr_no_wi = copy.deepcopy(w_arr)
        w_arr_no_wi.remove(w_v_zip[i][0])
        val_arr_no_vi = copy.deepcopy(val_arr)
        val_arr_no_vi.remove(w_v_zip[i][1])
        sol1 = w_v_zip[i][1] + knapsack_without_repetitions_recursive(capacity - w_arr[i], w_arr_no_wi, val_arr_no_vi)

        #OUTER_CASE2: w_arr[i] might not be in our solution
        ## In this case answer = knapsack_without_repetitions(capacity,w_arr.remove(w_v_zip[i][0])), val_arr.remove(w_v_zip[i][1]))
        sol2 = knapsack_without_repetitions_recursive(capacity, w_arr_no_wi, val_arr_no_vi)

        ##Now we just need to find max of above two OUTER_CASES

        if max(sol1,sol2) > max_value:
            max_value =max(sol1,sol2)

    return max_value


w_arr = [2,3,4,6]
val_arr = [9,14,16,30]

# print(knapsack_without_repetitions_recursive(10, w_arr, val_arr))

def knapsack_without_repetitions_dynamic(capacity, w_arr, val_arr):

    # need to do sanitization that both have same size, no neg values and capacity is positive as well

    w_v_array = [[0 for _ in range(len(w_arr)+1)] for __ in range(capacity+1)]

    for i in range(len(w_arr)):
        w_v_array[0][i] = 0
        w_v_array[i][0] = 0

    for i in range(1,len(w_arr)+1):

        for w in range(1,capacity+1):

            w_v_array[w][i] = w_v_array[w][i-1]

            if w_arr[i-1] <= w:
                val = w_v_array[w-w_arr[i-1]][i-1] + val_arr[i-1]
                w_v_array[w][i] = max(w_v_array[w][i], val)

    return w_v_array[capacity][len(w_arr)]


print(knapsack_without_repetitions_dynamic(10, w_arr, val_arr))