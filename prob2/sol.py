from functools import reduce

inp = str(input('Entr list'))
arr = list(map(lambda x: int(x), inp.split()))
prod = reduce(lambda x, y: x * y, arr)
ans = list(map(lambda x: int(prod / x), arr))
print('_________\nAnswer\n', ans, '\n_________')



# To Do: 
# Follow-up: what if you can't use division?