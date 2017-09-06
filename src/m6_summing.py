"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Riley McCrocklin.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_cosines()
    test_sum_square_roots()


def test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')
    expected = 0.13416
    answer = sum_cosines(3)
    print('Test 2 expected: ', expected)
    print('       actual:   ', answer)
    expected = -0.51948
    answer = sum_cosines(4)
    print('Test 2 expected: ', expected)
    print('       actual:   ', answer)
    expected = -0.23581
    answer = sum_cosines(5)
    print('Test 3 expected: ', expected)
    print('       actual:   ', answer)


def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    if n < 0:
        n = -n
    y = 0
    for k in range(n+1):
        x = math.cos(k)
        y = y+x
    return y


    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


def test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # Done: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')
    expected = 11.854408
    answer = sum_square_roots(5)
    print('Test 1 expected: ', expected)
    print('       actual:   ', answer)
    expected = 19.06
    answer = sum_square_roots(7)
    print('Test 2 expected: ', expected)
    print('       actual:   ', answer)
    expected = 5.8637
    answer = sum_square_roots(3)
    print('Test 3 expected: ', expected)
    print('       actual:   ', answer)


def sum_square_roots(n):
    if n < 0:
        n = -n
    y = 0
    for k in range(n+1):
        x = k*2
        x = x**(1/2)
        y = y + x
    return y

    # ------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
