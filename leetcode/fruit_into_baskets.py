def total_fruits_1(trees):
    '''O(1) space and O(n) time <- best possible'''

    if len(trees) <= 2:
        # len 2 is however already taken care of by the algorithm
        return len(trees)

    max_fruit = 1  # min trees is 1, this variable will keep on updating as we progress through array
    run_counter = 0  # stores how much variation is there in next val as compared to current val in trees array
    # next possible run_counter is always zero or negative of previous value
    res = 1  # final result

    for i in range(len(trees)):
        if i == 0 and i != len(trees) -1:
            run_counter = trees[1] - trees[0]
            continue

        if i != len(trees) - 1:
            next_diff = trees[i+1] - trees[i]

            if next_diff == 0:
                max_fruit += 1

            elif next_diff == -run_counter:
                run_counter = -run_counter
                max_fruit += 1

            elif run_counter == 0:
                run_counter = next_diff
                max_fruit += 1

            else:

                if max_fruit + 1 > res:
                    res = max_fruit + 1

                run_counter = next_diff
                max_fruit = 1
                j = i - 1

                # Handles the case when vals change but trees have similar values in prev indexes
                # max_fruit must then start with that prev index
                # see test case 6 [0,1,6,6,4,4,6]
                while j >= 0 and trees[j] == trees[i]:
                    max_fruit += 1
                    j -= 1


        else:
            if max_fruit + 1 > res:
                res = max_fruit + 1

    return res


def total_fruits_2(trees):

    if len(trees) <= 2:
        return len(trees)
    running_sum = 0
    res = 0
    basket = set()

    for i, val in enumerate(trees):
        if val in basket:
            running_sum += 1

        elif len(basket) < 2:
            basket.add(val)
            running_sum += 1

        else:
            if running_sum > res:
                res = running_sum

            prev = trees[i- 1]
            basket = set()
            basket.add(val)
            basket.add(prev)
            running_sum = 2
            j = i-2
            while j >= 0 and trees[j] == prev:
                running_sum += 1
                j -= 1

        # print(f"trees:{trees},i:{i}, val:{val}, basket:{basket}, running_sum:{running_sum}, res:{res}")

    return res if res > running_sum else running_sum

