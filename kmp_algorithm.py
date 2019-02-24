def computePrefixFunction(P):
    s = [0]*len(P)
    border = 0
    while_loop_counter = 0
    for i in range(1,len(P)):
        while (border > 0) and P[i] != P[border]:
            print(f"while_loop_counter:{while_loop_counter}, i;{i}")
            while_loop_counter+=1
            # border -= 1
            ## Take the longest border of our current border
            ## Our current border ends in position: border - 1
            border = s[border-1]

        ## Breaking out of the loop may be due to 2 conditions:
        ##Condition1: border == 0 and values still don't match
        ##Condition2: border >=0 and values match
        if P[border] == P[i]:
            border += 1
        else:
            border = 0

        s[i] = border

    print(s)
    return s


# print(computePrefixFunction('abababcaab'))


def kmp_algorithm(text, pattern):
    new_str = pattern+"$"+text ## assuming $ doesn't appear in text or pattern
    ## $ sign ensures that no value in array returned by prefix function is greater than |pattern|
    prefix_array = computePrefixFunction(new_str)
    result = [i-2*len(pattern) for i in range(len(new_str)) if prefix_array[i] == len(pattern)]
    return result


# print(kmp_algorithm('abracadabra','abra'))
# print(computePrefixFunction('ACATACATACACA')) # gives incorrect result when border -=1 instead of border = s[border-1]
print(computePrefixFunction('ACATACATACACA'))