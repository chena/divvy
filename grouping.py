"""
- get all combinations of groups (N groups of M out of N * M people)
- for each possible groupings, use a heuristic to measure the "total" happiness of each set
- get the most optimal final groupings based on the results
"""
def choose_formula(n , k):
	return fact(n) / (fact(k) * fact(n - k))

def choose__k(n, k):
	if n == k or k == 0:
		return 1
	if n == 0:
		return 0
	return choose__k(n - 1, k) + choose__k(n - 1, k - 1)

def choose_k_list(lst, k):
	if len(lst) == k:
		return [lst]
	if k == 0:
		return [[]]
	return choose_k_list(lst[1:], k) + [[lst[0]] + sublst for sublst in choose_k_list(lst[1:], k - 1)]

def choose_groups_k(n, k):
	"""
	find the number of groupings from n items with a group size of k (total of n/k size)
	"""
	if n < 1 or n == k:
		return 1
	if k == 1:
		return n
	# use one person as a pivot, then choose the rest of people in that group
	# for the rest of people, do the same
	return choose_k(n - 1, k - 1) * choose_groups_k(n - k, k)

def choose_groups(lst, k):
	"""
	find combinations of size k from the list, assuming that len(list)/k is a whole number
	"""
	# FIXME: this is not right
	if len(lst) == k:
		return [lst]
	if k == 0:
		return [[]]
	fgroup = choose_k_list(lst[1:], k - 1)
	rest = [item for item in lst if item not in fgroup]
	for subgroup in choose_groups(rest, k):
		print fgroup + subgroup  
		
"""
print choose_groups_num(6, 2)
print choose_groups_num(4, 2)
print choose_groups_num(6, 3)
print choose_groups_num(10, 2)
"""
choose_groups([1, 2, 3, 4], 2)