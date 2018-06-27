
'''
Working - June 27 2018
'''
def get_earliest(*args, omit=0):
    if omit == 3:
        return args[0]
    arr = [arg.split('/') for arg in args]
    iteration = [2, 0, 1]

    counter = 0
    min_index = counter
    eligible_candidates = set()
    omission_counter = 0
    next_omit = 0
    for i in iteration:
        if omission_counter != omit:
            omission_counter += 1
            continue

        if len(eligible_candidates) is 0:
            min_val = int(arr[min_index][i])
            while(counter < len(arr)-1):
                print("current counter: {}\t min_index:{}\t min_val:{}".format(counter,min_index,min_val))
                if arr[counter][i] == arr[counter+1][i]:
                    print("this element: {} same as next element: {}. Inc counter".format(arr[counter][i],arr[counter+1][i]))
                    if arr[counter][i] == arr[min_index][i]:
                        print("Adding entry to eligible candidates")
                        eligible_candidates.add(args[counter])
                        eligible_candidates.add(args[counter+1])
                        next_omit = iteration.index(i) + 1
                    counter += 1
                    continue
                else:
                    prev_min = min_val
                    print("comparing {}, {}, {}".format(int(arr[counter][i]), min_val, int(arr[counter + 1][i])))
                    min_val = min(int(arr[counter][i]), min_val, int(arr[counter+1][i]))
                    if prev_min == min_val:
                        print("min value unchanged")
                        pass
                    elif min_val == int(arr[counter][i]):
                        min_index = counter
                        print("1-min value updated: {} min_index updated: {}".format(arr[counter], min_index))
                    else:
                        min_index = counter+1
                        print("2-min value updated: {} min_index updated: {}".format(arr[counter], min_index))


                    if counter == len(arr)-2:
                        print("returning")
                        return args[min_index]
                    counter +=1
        else:
            print(eligible_candidates)
            print(type(eligible_candidates))
            return get_earliest(*eligible_candidates, omit=next_omit)




    return args[0]



# print(get_earliest("01/24/2007","01/21/2008","02/29/2009","02/30/2006","02/28/2006","02/29/2006"))
