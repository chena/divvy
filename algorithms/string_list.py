"""
1. Compress a string. Ex: aabcccccaaa to a2blc5a3
2. Reverse a string in place 
3. Determine if two strings are anagram of each other
4. Determine if a string has all unique characters
5. Remove all duplicates in a string
6. Replace all space with %20 without creating a new string
7. Rotate an NxM matrix by 90 degree
8. Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
9. Check if one string is a rotation of the other
10. Find the most common string in a list
11. Find largest k elements in an array without sorting
12. Write an algorithm to find all pairs of integers that sum to a specific value in an array
"""
from collections import Counter

def compress(string):
	out = []
	curr = string[0]
	count = 0

	for s in string:
		if s == curr:
			count += 1
		else:
			out.append(curr + str(count))
			count = 1
			curr = s

	# append the last character and its count
	out.append(curr + str(count))
	return ''.join(out)

"""
without doing string[::-1]
"""
def reverse(string):
	start = 0
	end = len(string) - 1
	lst = list(string)

	while start < end:
		temp = lst[start]
		lst[start] = lst[end]
		lst[end] = temp
		start += 1
		end -= 1

	return ''.join(lst)

def reverse_recursive(string):
	length = len(string)
	if length == 1:
		return string
	return string[length-1] + reverse_recursive(string[:length-1])

"""
Using a dictionary with 2 scans = linear time
Sort and compare = O(N Log N)
"""
def is_anagram(str1, str2):
	if len(str1) != len(str2):
		return False

	counts = Counter(str1)

	for c in str2:
		if not c in counts or counts[c] == 0:
			return False
		counts[c] -= 1

	return True

"""
Check substring for each char = O(n^2)
Keeping a dictionary = linear
"""
def string_unique_n2(string):
	for i, c in enumerate(string):
		if c in string[i + 1:]:
			return False
	return True

def string_unique_n(string):
	counts = {}
	for c in string:
		if c in counts:
			return False
		counts[c] = 1
	return True

"""
naive approach = O(n^2)
if we don't need to preserve order, then we can simply return the set
"""
def remove_dup_naive(string):
	index = 0
	lst = list(string)
	while index < len(lst) - 1:
		sub = lst[index + 1:]
		item = lst[index]
		if item in sub:
			lst.remove(item)
		else:
			index += 1
	return ''.join(lst)

def remove_dup_set(string):
	return ''.join(set(string))

def replace_space(string):
	return ''.join([s if s != ' ' else '%20' for s in string])

"""
[[1 2 3], 
[4 5 6]]

[[4 1], 
[5 2], 
[6 3]]

we want to first reverse the sublists, 
then zip each pair by passing in the sublists as argument
"""
def rotate_mat(matrix):
	return zip(*matrix[::-1])

def set_mat_zero(matrix):
	if len(matrix) < 1:
		return

	rows, cols = [], []
	row_num = len(matrix)
	col_num = len(matrix[0])

	for i in range(row_num):
		for j in range(col_num):
			if matrix[i][j] == 0:
				rows.append(i)
				cols.append(j)

	for i in range(row_num):
		for j in range(col_num):
			if i in rows or j in cols:
				matrix[i][j] = 0

	return matrix

def check_rotated(str1, str2):
	if len(str1) != len(str2):
		return False
	return str2 in str1 + str1

def most_common(lst):
	# one line approach
	return max(set(lst), key=lst.count)
	"""
	counts = Counter(lst)
	max_count = sorted(counts.values())[len(counts) - 1]
	for k ,v in counts.items():
		if v == max_count:
			return k
	"""

def largest_k_sort(lst, k):
	lst.sort()
	return lst[-k:]

def largest_k_select(lst, k):
	size = len(lst)
	for i in range(size):
		max_ind = i
		max_val = lst[i]
		for j in range(i + 1, size):
			val = lst[j]
			if val > max_val:
				max_ind = j
				max_val = val
		lst[max_ind] = lst[i]
		lst[i] = max_val
	return lst[:k]

def find_sum_pair(lst, s):
	start, end = 0, len(lst) - 1
	pairs = []
	lst.sort()

	while start < end:
		left, right = lst[start], lst[end]
		total = left + right
		if total == s:
			pairs.append((left, right))
			start += 1
			end -= 1
		elif total < s:
			start += 1
		else:
			end -= 1

	return pairs

def check_palindrome(string):
	start = 0
	end = len(string) - 1

	while start < end:
		if string[start] != string[end]:
			return False
		start += 1
		end -= 1
	return True

def hamming_dist(str1, str2):
	"""
	assuming str1 and str2 have the same length
	"""
	return sum([f != s for (f, s) in zip(str1, str2)])


def best_profit(prices):
	"""
	I have an array stockPricesYesterday where
	The values are the price of Apple stock at that time, in dollars.
	Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
	"""
	min_price = prices[0]
	max_profit = 0
	for price in prices:
		min_price = min(min_price, price)
		max_profit = max(max_profit, price - min_price)
	return max_profit


			

