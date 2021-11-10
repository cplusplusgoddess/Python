"""
Fibonacci sequences using generators

"""
import collections



def fibonacci2(n: int) -> int:
	""" 
	generator via recursion
	""" 
    if n <= 0:
        return 0
    if n == 1:
        return 1
    yield fibonacci2(n-1) + fibonacci2(n-2)


def fibonacci(max_sequence):
    a, b = 0, 1
    # while a < max_sequence:
    for n in range(0, max_sequence):
        yield a
        a, b = b, a+b


# print(list(fibonacci2(9))) Note: This fails although documented to work
fib_numbers = fibonacci2(9)
print(fib_numbers)			# This returns the address of generator in addition to list
for n in fibonacci(9):
    print(n)


# This was another case considered for implementing via yield but ended up
# being a practice for namedtuple

Fraction = collections.namedtuple('Fraction', ['numerator', 'denominator'])


def frac_div(a: Fraction, b: Fraction) -> int:
    return (int)(a.numerator * b.denominator / a.denominator / b.numerator)


first = Fraction(30, 5)
second = Fraction(19, 38)
print(frac_div(first, second))
