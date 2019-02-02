class Node:
	def __init__(self, val=None, next=None):
		self.val = val
		self._next = [] ## why can't it be set in the first place?
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
		# print("looping through pattern: {}".format(pattern))
		current_node = root
		# print("current_node set to root:{}".format(root))

		for p in pattern:
			# print("adding: {}".format(p))
			# print("root next_vals: {}".format(root.next_vals))
			# print("current_node.next_vals: {}".format(current_node.next_vals))
			if p in current_node.next_vals:
				# print("{} exists inside {} next vals:{}".format(p, current_node, current_node.next_vals))
				for child in current_node.next:
					if p == child.val:
						current_node = child
			else:
				new_node = Node(p)
				current_node.next = new_node
				# print("current_node.next:{}".format(current_node.next))
				# print("current_node.next_vals:{}".format(current_node.next_vals))
				current_node = new_node
				# print("current_node is now node: {}".format(current_node))
				# print("current_node.next: {}".format(current_node.next))
				# print("current_node.next_vals:{}".format(current_node.next_vals))
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


## trie using dict of dicts

# >>> _end = '_end_'
# >>>
# >>> def make_trie(*words):
# ...     root = dict()
# ...     for word in words:
# ...         current_dict = root
# ...         for letter in word:
# ...             current_dict = current_dict.setdefault(letter, {})
# ...         current_dict[_end] = _end
# ...     return root


# def in_trie(trie, word):
# ...     current_dict = trie
# ...     for letter in word:
# ...         if letter in current_dict:
# ...             current_dict = current_dict[letter]
# ...         else:
# ...             return False
# ...     else:
# ...         if _end in current_dict:
# ...             return True
# ...         else:
# ...             return False

## also
# class Node:
# 	def __init__(self, label=None, data=None):
# 		self.label = label
# 		self.data = data
# 		self.children = dict()
#
# 	def addChild(self, key, data=None):
# 		if not isinstance(key, Node):
# 			self.children[key] = Node(key, data)
# 		else:
# 			self.children[key.label] = key
#
# 	def __getitem__(self, key):
# 		return self.children[key]
#
#
# class Trie:
# 	def __init__(self):
# 		self.head = Node()
#
# 	def __getitem__(self, key):
# 		return self.head.children[key]
#
# 	def add(self, word):
# 		current_node = self.head
# 		word_finished = True
#
# 		for i in range(len(word)):
# 			if word[i] in current_node.children:
# 				current_node = current_node.children[word[i]]
# 			else:
# 				word_finished = False
# 				break
#
# 		# For ever new letter, create a new child node
# 		if not word_finished:
# 			while i < len(word):
# 				current_node.addChild(word[i])
# 				current_node = current_node.children[word[i]]
# 				i += 1
#
# 		# Let's store the full word at the end node so we don't need to
# 		# travel back up the tree to reconstruct the word
# 		current_node.data = word
#
# 	def has_word(self, word):
# 		if word == '':
# 			return False
# 		if word == None:
# 			raise ValueError('Trie.has_word requires a not-Null string')
#
# 		# Start at the top
# 		current_node = self.head
# 		exists = True
# 		for letter in word:
# 			if letter in current_node.children:
# 				current_node = current_node.children[letter]
# 			else:
# 				exists = False
# 				break
#
# 		# Still need to check if we just reached a word like 't'
# 		# that isn't actually a full word in our dictionary
# 		if exists:
# 			if current_node.data == None:
# 				exists = False
#
# 		return exists
#
# 	def start_with_prefix(self, prefix):
# 		""" Returns a list of all words in tree that start with prefix """
# 		words = list()
# 		if prefix == None:
# 			raise ValueError('Requires not-Null prefix')
#
# 		# Determine end-of-prefix node
# 		top_node = self.head
# 		for letter in prefix:
# 			if letter in top_node.children:
# 				top_node = top_node.children[letter]
# 			else:
# 				# Prefix not in tree, go no further
# 				return words
#
# 		# Get words under prefix
# 		if top_node == self.head:
# 			queue = [node for key, node in top_node.children.iteritems()]
# 		else:
# 			queue = [top_node]
#
# 		# Perform a breadth first search under the prefix
# 		# A cool effect of using BFS as opposed to DFS is that BFS will return
# 		# a list of words ordered by increasing length
# 		while queue:
# 			current_node = queue.pop()
# 			if current_node.data != None:
# 				# Isn't it nice to not have to go back up the tree?
# 				words.append(current_node.data)
#
# 			queue = [node for key, node in current_node.children.iteritems()] + queue
#
# 		return words
#
# 	def getData(self, word):
# 		""" This returns the 'data' of the node identified by the given word """
# 		if not self.has_word(word):
# 			raise ValueError('{} not found in trie'.format(word))
#
# 		# Race to the bottom, get data
# 		current_node = self.head
# 		for letter in word:
# 			current_node = current_node[letter]
#
# 		return current_node.data
#
#
# if __name__ == '__main__':
# 	""" Example use """
# 	trie = Trie()
# 	words = 'hello goodbye help gerald gold tea ted team to too tom stan standard money'
# 	for word in words.split():
# 		trie.add(word)
# 	print "'goodbye' in trie: ", trie.has_word('goodbye')
# 	print trie.start_with_prefix('g')
# 	print trie.start_with_prefix('to')


