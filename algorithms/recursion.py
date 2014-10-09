"""
1. Stairs problem
2. Taxi problem
3. Fibonacci
4. Find all permutations of a String
5. Solve N choose K
6. Implement recursive version of sum
7. Find the largest number in a list
8. Get the item at the last index of a list, without using lastIndexOf
9. Find all subsets of a set (think binary)
10. Print all valid paren for n pairs of paren (increment, increment)
"""

def go_up_stairs(n):
	"""
	how many ways are there to go up a stair given number of steps to climb
	going one, two, or three steps at a time
	"""
	if n < 0:
		return 0
	if n == 0:
		return 1
	return go_up_stairs(n-1) + go_up_stairs(n-2) + go_up_stairs(n-3)

def taxi_routes(n, m):
	"""
	how many ways are there for a taxi driver to get from the top left of 
	a n x m grid city to the bottom right
	"""
	if n == 0 or m == 0:
		return 1
	return taxi_routes(n, m - 1) + taxi_routes(n - 1, m)

def fib(num):
	if (num < 2):
		return num
	return fib(num - 1) + fib(num - 2)

def permutate(input):
	"""
	find all permutations of a given string
	"""
	size = len(input)
	if size == 1:
		return [input]

	clist = list(input)
	output = []
	for i in range(size):
		clist_copy = clist[:]
		c = clist[i]
		del clist_copy[i]
		for p in permutate(''.join(clist_copy)):
			output.append(c + p)
	return set(output)

"""
find cloest points given a list of points
"""