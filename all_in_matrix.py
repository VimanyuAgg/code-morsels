import unittest
import copy

def rotate_anticlockwise(shape):
	return [ [ shape[y][x]
			for y in range(len(shape)) ]
		for x in range(len(shape[0]) - 1, -1, -1) ]


def rotate_clockwise(shape):
	_shape = copy.deepcopy(shape)
	_shape = _shape[::-1]
	return list(map(list,zip(*_shape)))

def rotate_anticlockwise2(shape):
	_shape = copy.deepcopy(shape)
	for i in range(len(shape)):
		_shape[i] = _shape[i][::-1]

	return list(map(list,zip(*_shape)))

def rotate_anticlockwise3(shape):
	## Rows become cols and cols become rows
	rows = len(shape)
	cols = len(shape[0])

	new_m = [[0 for _ in range(rows)] for __ in range(cols)]

	for i in range(cols-1,-1,-1):
		for j in range(rows):
			new_m[cols-1-i][j] = shape[j][i]

	return new_m


class TestAllInMatrix(unittest.TestCase):

	def test_clockwise(self):
		shape = [[1, 2, 3], [-1, -2, -3]]
		self.assertEqual(rotate_clockwise(shape),[[-1, 1], [-2, 2], [-3, 3]])

	def test_anticlockwise1(self):
		shape = [[1, 2, 3], [-1, -2, -3]]
		self.assertEqual(rotate_anticlockwise(shape),[[3, -3], [2, -2], [1, -1]])

	def test_anticlockwise2(self):
		shape = [[1, 2, 3], [-1, -2, -3]]
		self.assertEqual(rotate_anticlockwise2(shape), [[3, -3], [2, -2], [1, -1]])

	def test_anticlockwise3(self):
		shape = [[1, 2, 3], [-1, -2, -3]]
		self.assertEqual(rotate_anticlockwise3(shape), [[3, -3], [2, -2], [1, -1]])


if __name__ == "__main__":
	unittest.main()


