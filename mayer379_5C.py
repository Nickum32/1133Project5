# CSci 1133 HW 5
# Nicholas Mayer
# HW Problem B
#
# Square digit summation tool using recursive function
#

def SquareNSum(num, positive=1): # num is the given input value, positive is an indicator of whether the initial value given was positive (1) or negative (-1)
    n = abs(num) # regular operators won't work correctly on negative numbers, so abs() is needed
    if num < 0:
        positive = -1 # the operators won't work correctly on negative, so this will be passes through each call to indicate whether the initial value was negative
    if n < 10: # base case for a single digit number
        return positive*(n**2) 
    else:
        return (positive*(n%10)**2) + SquareNSum(positive*(n//10), positive) # recurrence case for any number with 2 or more digits
