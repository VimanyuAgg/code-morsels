def compact(input_list):
    result  = []
    i=0
    while i < len(input_list):
        print("i:{}".format(i))
        flag = False
        while (i < len(input_list) - 1) and input_list[i] == input_list[i+1]:
            i += 1
            flag = True
        if i == 0:
            result.append(input_list[i])
        elif flag:
            result.append(input_list[i-1])
        else:
            result.append(input_list[i])
        i+=1

    return result


print(compact([1,2,3]))