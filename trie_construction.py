class Node:
	def __init__(self, val=None, next=None):
		self.val = val
		self._next = []
		if next is not None:
			print("hi: {}".format(self))
			self.next = next

	@property
	def val(self):
		return self._val

	@property
	def next(self):
		# print("{} next called: {}".format(self, self._next))
		return self._next

	@property
	def next_vals(self):
		# print("{} next_vals called".format(self))
		if self.is_leaf:
			return set()
		return set([n.val for n in self.next])


	@property
	def is_leaf(self):
		# print("{}: is_leaf is called".format(self))
		return self.next == []

	@val.setter
	def val(self, new_val):
		# print("val_setter is called")
		self._val = new_val


	@next.setter
	def next(self, next_node):
		# print("{}: next_setter is called".format(self))
		# print("{}: next_setter before next val {}".format(self,self.next))
		self._next.append(next_node)
		# print("{}: next_setter after next val {}".format(self, self.next))


	def __repr__(self):
		return f"Node ({self.val})"
	#
	def __eq__(self, other):
		try:
			return self.val == other.val
		except AttributeError:
			return NotImplemented

def trie_construction(patterns):
	root = Node()
	for pattern in patterns:
		print("looping through pattern: {}".format(pattern))
		current_node = root
		print("current_node set to root:{}".format(root))

		for p in pattern:
			print("adding: {}".format(p))
			print("root next_vals: {}".format(root.next_vals))
			print("current_node.next_vals: {}".format(current_node.next_vals))
			if p in current_node.next_vals:
				print("{} exists inside {} next vals:{}".format(p, current_node, current_node.next_vals))
				for child in current_node.next:
					if p == child.val:
						current_node = child
			else:
				new_node = Node(p)
				current_node.next = new_node
				print("current_node.next:{}".format(current_node.next))
				print("current_node.next_vals:{}".format(current_node.next_vals))
				current_node = new_node
				print("current_node is now node: {}".format(current_node))
				print("current_node.next: {}".format(current_node.next))
				print("current_node.next_vals:{}".format(current_node.next_vals))
	return root


def trie_helper(text, root):
	current = root
	found_val = ""
	for t in text:
		if t in current.next_vals:
			for child in current.next:
				if child.val == t:
					found_val += t
					current = child
					break
			if current.is_leaf:
				print("{}: found!".format(found_val))
				return
		else:
			return


def trie_matching(text, list_of_patterns):
	root = trie_construction(list_of_patterns)
	while len(text) != 0:
		trie_helper(text, root)
		if len(text) == 1:
			print("done")
			return
		else:
			text = text[1:]