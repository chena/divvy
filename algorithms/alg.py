from collections import defaultdict

def check_anagram(str1, str2):
	if (len(str1) != len(str2)):
		return False

	count = defaultdict(int)
	for s in str1:
		count[s] += 1
	for s in str2:
		if not count.has_key(s) or count[s] == 0:
			return False
		count[s] -= 1
	return True

def reverse_str(input):
	return input[::-1]

def max(numbers, largest_so_far=0):
    if numbers == []:
        return largest_so_far
    next_num = numbers[0]
    if next_num > largest_so_far:
    	return max(numbers[1:], next_num)
    return max(numbers[1:], largest_so_far)

def sum(numbers):
	if len(numbers) == 1:
		return numbers[0]
	return numbers[0] + sum(numbers[1:])

def last_index(numbers, n):
	"""
	returns the last index of number in a list
	"""
	if n in numbers:
		ind = numbers.index(n)
		numbers[ind] = None
		return max([ind, last_index(numbers, n)]) 
	return -1

def combinations_repeat(n, k):
	if n == 1:
		return k
	return k * combinations_repeat(n - 1, k)

#print permutate('abc')
#print combinations_repeat(2, 3)