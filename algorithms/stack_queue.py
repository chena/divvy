class Stack(object):
	def __init__(self, items=[]):
		self.items = items

	def push(self, item):
		self.items.append(item)

	def peek(self):
		if self.items:
			return self.items[len(self.items) - 1]

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

class MyQueue(object):
	def __init__(self):
		self.inp = []
		self.out = []

	def enqueue(self, item):
		self.inp.append(item)

	def dequeue(self):
		if not self.out:
			while self.inp:
				self.out.append(self.inp.pop())
		return self.out.pop()

class SortedStack(object):
	def __init__(self):
		self.stack = []

	def push(self, item):
		if self.stack and item < self.peek():
			self.stack.insert(0, item)
		else:
			self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[len(self.stack) - 1]

	def get_largest(self):
		return self.pop() 

def hanoi(disks, source, dest, temp):
	"""
	solve the Towers of Hanoi problem
	- move n - 1 disks from source to temp
	- move nth disk from source to dest
	- move n - 1 disks from temp to dest
	"""
	if not disks:
		return
	else:
		hanoi(disks[1:], source, temp, dest)
		move(disks[0], source, dest)
		hanoi(disks[1:], temp, dest, source)

def move(disk, f, to):
	print "Move {} from tower {} to tower {}".format(disk, f, to) 

def balanced_brackets(string):
	st = Stack()
	mapping = {'{': '}', '(': ')', '[': ']'}

	for b in string:
		if b in mapping.keys():
			st.push(mapping[b])
		else: # closing bracket
			if st.peek() != b:
				return False
			st.pop()

	if st.size() > 0:
		return False

	return True

hanoi([3, 2, 1], 'source', 'dest', 'tmp')

