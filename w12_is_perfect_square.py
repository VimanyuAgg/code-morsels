from math import sqrt
from decimal import Decimal, Context, localcontext
import cmath

def is_perfect_square_original(n, complex = None):
	if complex is None:
		try:
			if n < 0:
				return False

			for x in range(0,n/2):
				if x**2 == n:
					return True
				return False
		except TypeError as e:
			raise TypeError("Invalid Types")



def is_perfect_after_1(n):
	"""
	Returns true if n is a perfect square
	Raises TypeError is n is not integer, float but string etc.
	Raises ValueError if n is negative
	sqrt returns floating point numbers - so problem for HUGE inputs!
	"""
	return sqrt(n) % 1 == 0  # %1 == 0 checks for integer-ness


def is_perfect_after_2(n):
	"""
	Returns true if n is a perfect square
	Returns False for negative numbers instead of raising ValueError
	Raises TypeError if n is string etc.
	Problem for HUGE numbers as sqrt returns floating point number
	"""
	if n < 0:
		return False
	return int(sqrt(n)) ** 2 == n


def is_perfect_after_3(n):
	"""
	Returns true if in is a perfect square
	~~Easier to ask forgiveness than permission~~
	Returns False for negative n
	More readable .is_integer()
	Raises TypeError when n is string etc.
	Problem if n is HUGE! as sqrt returns floating point which has a max precision
	"""
	try:
		return sqrt(n).is_integer()
	except ValueError as e:
		return False


def is_perfect_after_4(n):
	"""
	Returns true if n is a perfect square
	Doesn't use math.sqrt()
	"""
	return int(n ** (0.5)) ** 2 == n


def is_perfect_after_5(n):
	"""
	Returns true if n is a perfect square
	Works for HUGE numbers as Decimal class has a better precision than math library and
	it's default precision (28) can be updated
	"""
	if n < 0:
	# This check is now needed because negative numbers do not raises
	# ValueError but decimal.invalidOperation now
		return False

	digit_in_n = len(str(n))
	with localcontext(Context(prec=digit_in_n * 2)):
		return int(Decimal(n).sqrt())**2 == n

from decimal import Decimal, Context, localcontext



def is_perfect_after_6_complex(n, *, complex=False):
	"""
	Works for complex numbers - * forces complex to be a keyword only argument
	Works for large inputs
	"""
	if complex:
		complex_root = cmath.sqrt(n)
		return complex_root.real.is_integer() and complex_root.imag.is_integer()
	else:
		if n < 0:
			return False
		digit_num = len(str(n))
		with localcontext(Context(prec=digit_num * 2)):
			return int(Decimal(n).sqrt())**2 == n
			# return Decimal(n).sqrt().is_integer() #AttributeError: 'decimal.Decimal' object has no attribute 'is_integer'
