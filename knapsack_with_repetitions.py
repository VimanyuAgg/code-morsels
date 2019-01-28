def knapsack_with_repetitions(items_val,item_weights,max_weight):
    knapsack_vals = [0] # ith index stores values of knapsacks with max_weight [i]
    for w in range(1, max_weight+1):
        print("** iterating for w: {}".format(w))
        knapsack_val = 0 # value of knapsack with max_weight w
        print(f"knapsack_val: {knapsack_val}")

        for i in range(len(items_val)):
            print("checking for item: {}, weight: {}, value:{}".format(i, item_weights[i], items_val[i]))
            if item_weights[i] <= w:
                print("item_weight[{}]: {} <= {}".format(i,item_weights[i],w))
                val = knapsack_vals[w - item_weights[i]] + items_val[i]
                print(f"val = knapsack_vals[{w - item_weights[i]}] + {items_val[i]}")

                print(f"Checking if val:{val} > knapsack_val:{knapsack_val}")
                if val > knapsack_val:
                    print("check successfull")
                    knapsack_val = val
                    print(f"knapsack_val: {knapsack_val}")

        print("max weight of knapsack with w: {} is {}".format(w,knapsack_val))
        knapsack_vals.append(knapsack_val)

    return knapsack_vals[-1]