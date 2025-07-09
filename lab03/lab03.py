SOURCE_FILE = __file__


def double_eights(n):
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return False
    if n % 10 == 8:
        return n // 10 % 10 == 8 or double_eights(n // 10)
    else:
        return double_eights(n // 10)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    return gcd(b % a, a)
    


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    if column > row:
        return 0
    elif row == 0 and column == 0:
        return 1
    elif column == 0:
        return pascal(row - 1, column)
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)
    
def fac(m):
    if m == 1:
        return 1
    else:
        return m * fac(m - 1)
        
def choose(m,n):
    return fac(m)/fac(n)/fac(m - n)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def recur(x, y):
        if x == 1 and y == 1:
            return 1
        if x < 0 or y < 0:
            return 0
        return recur(x - 1, y) + recur(x, y - 1)
    return recur(m,n)