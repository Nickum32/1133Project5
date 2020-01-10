# CSci 1133 HW 5
# Nicholas Mayer
# HW Problem B
#
# This program will utilize recursion to calculate the series ((-1)^(n-1))/n for a
# given n.
# Base case: n = 1, return 1
# Recurrence relationship: n > 1 = f(n-1)
#
def f(n):
    if n <= 0: # base case checks for 0 or negative values
        return 0
    else:
        term = (-1)**(n-1)/n
        return term + f(n-1) # recurrence relationship calls the next value in the series
