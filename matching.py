import json
from collections import OrderedDict

"""
Stable matching problem scenario:
- 2 groups of N people (eg. students and mentors), each student has a ranked list of N for their mentor preferences
- each student, say s, first picks their top ranked mentor m
	- if mentor m is available, then s is assigned
	- else (the mentor is already matched), then
		- if m prefers s over the current match c, then s is macthed and c is out
		- otherwise s goes to the next ranked mentor and repeats the step
- the algorithm terminates when evey student is matched with a mentor
"""
class Matcher(object):

	def __init__(self, propose_group, cand_group, group_size):
		self.group_size = group_size
		self.propose_group = propose_group
		self.cand_group = cand_group 

	def match(self):
		if len(self.propose_group) != self.group_size or len(self.cand_group) != self.group_size:
			raise ValueError("Each group must have %d people" % self.group_size)
		final_group = []
		while self.get_free():
			# get the current proposer and mark its top candidate as visited
			p = self.get_free()
			cname = p.get_top_name()
			p.ranked_list[cname] = True

			# get the target candidate and get its current match
			cand = self.find_by_name(self.cand_group, cname)
			cmatch = cand.match # handle error

			# assign if the candidate does not have a match
			if not cmatch:
				p.match = cname
				cand.match = p.name
			else:
				if cand.compare(p.name, cmatch) < 0: # lower rank is better
					p.match = cname
					cand.match = p.name
					pp = self.find_by_name(self.propose_group, cmatch)
					pp.match = None

		for p in self.propose_group:
			print p.name, p.match

	# FIXME: this doesn't seem very efficient?
	def get_free(self):
		for p in self.propose_group:
			if not p.match: 
				return p

	def find_by_name(self, group, name):
		for p in group:
			if p.name == name:
				return p

class Participant(object):

	def __init__(self, name):
		self.name = name
		self.ranked_list = {}
		self.match = None

	def __str__(self):
		return self.name

	def set_ranked_list(self, lst):
		self.ranked_list = OrderedDict((p, False) for p in lst)

class Proposer(Participant):
	# FIXME: use a rank index instead
	def get_top_name(self):
		"""
		get the participant's top chocie that hasn't been proposed
		"""
		for (k, v) in self.ranked_list.items():
			if not v: 
				return k

class Candidate(Participant):
	def compare(self, p1, p2):
		return self.ranked_list.keys().index(p1) - self.ranked_list.keys().index(p2)

if __name__ == '__main__':
	group1, group2 = [], []
	data = json.loads(open('people.json').read())
	
	for prop in data['proposers']:
		p = Proposer(prop['name'])
		p.set_ranked_list(prop['ranked_list'])
		group1.append(p)

	for cand in data['candidates']:
		c = Candidate(cand['name'])
		c.set_ranked_list(cand['ranked_list'])
		group2.append(c)

	matcher = Matcher(group1, group2, 4)
	matcher.match()


