inp = str(input('Entr list'))
arr = list(map(lambda x: int(x), inp.split()))
k = int(input('Entr k'))


# to_find = []
# for i in arr:
#   if i in to_find:
#     print('_________\nAnswer\n', True, i, '+', k-i, '=', k,'\n_________')
#     break
#   else:
#     to_find.append(k-i)
#     if i == arr[-1]:
#       print(False)

# For O(n) ->
to_find = {}

for i in arr:
	if i in to_find:
		print('_________\nAnswer\n', True, i, '+', k - i, '=', k,
		      '\n_________')
		break
	else:
		to_find[k - i] = True
		if i == arr[-1]:
			print(False)
