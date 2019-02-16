def make_change(n):
    denos = [25,10,5,1]
    return make_change_helper(n,denos, 0)

def make_change_helper(amount, denos, index):
    deno_amount = denos[index]
    if (index == len(denos)-1):
        remaining = amount % deno_amount
        return 1 if remaining == 0 else 0


    ways = 0
    my_amount = 0
    while my_amount <= amount:
        amount_remaining = amount - my_amount
        ways += make_change_helper(amount_remaining,denos,index+1)
        my_amount += deno_amount
    return ways


print(make_change(5))
