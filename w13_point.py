class Point_original:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return "Point({}, {}, {})".format(self.x, self.y, self.z)

	def __eq__(self, other_point):
		return (self.x == other_point.x) and (self.y == other_point.y) and (self.z == other_point.z)

	def __add__(self, other_point):
		return Point_original(self.x + other_point.x,
							  self.y + other_point.y,
							  self.z + other_point.z)

	def __sub__(self, other_point):
		return Point_original(self.x - other_point.x,
							  self.y - other_point.y,
							  self.z - other_point.z)

	def __mul__(self, other):
		return Point_original(self.x * other, self.y * other, self.z * other)


class Point_after:
	def __init__(self, x=0, y=0, z=0):
		self.x, self.y, self.z = x, y, z

	# def __repr__(self):
	# 	return f"Point({self.x}, {self.y}, {self.z})"

		# alternatively after implementing tuple unpacking
	def __repr__(self):
		return "Point({}, {}, {})".format(*self)

	# def __iter__(self):
	# 	return iter((self.x, self.y, self.z))

	# alternative __iter__
		# def __iter__(self):
		#	yield self.x
		#	yield self.y
		#	yield self.z

	# alternative __iter__
	def __iter__(self):
		yield from (self.x, self.y, self.z)

	def __add__(self, other):
		x1, y1, z1 = self
		x2, y2, z2 = other
		return Point_after(x1 + x2, y1 + y2, z1 + z2)

	def __sub__(self, other):
		x1, y1, z1 = self
		x2, y2, z2 = other
		return Point_after(x1 - x2, y1 - y2, z1 - z2)

	def __mul__(self, scalar):
		return Point_after(self.x * scalar, self.y * scalar, self.z * scalar)

	def __rmul__(self, scalar):
		return self.__mul__(scalar)

	# Alternatively
	# __rmul__ = __mul__

	# def __eq__(self, other):
	# 	return (tuple(self) == tuple(other))

	# def __eq__(self, other):
	# 	return ((*self,) == (*other,))

	# Alternatively
	def __eq__(self, other):
		return (self.x, self.y, self.z) == (other.x, other.y, other.z)

