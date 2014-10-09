
def to_binary(inp):
	parts = inp.split('.')
	num = parts[0]

	# convert num part
	binary = []
	num = int(num)
	while (num > 0):
		binary.append(str(num % 2))
		num = num / 2
	binary.reverse()

	if len(parts) > 1:
		binary.append('.')
		fract = parts[1]
		fract = float('0.' + fract)
		while fract > 0:
			d = fract * 2
			if d >= 1:
				binary.append('1')
				fract = d - 1
			else:
				binary.append('0')

	return ''.join(binary)

def subsets(set):
	pass