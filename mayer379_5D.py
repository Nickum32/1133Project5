# CSci 1133 HW 5
# Nicholas Mayer
# HW Problem D
#
# Doubles all characters within a list of strings
#
def helper(string):  # this is the function that parses through and doubles each character in a string
    if len(string) == 0: # base case is when no more characters are left to double
        return ''
    else:
        return string[0] + string[0] + helper(string[1:]) #recurrence relationship adds two copies of the first character and then calls the function on the rest of the string

def doubleStringList(lst, n=0): # this function pases each item in the list to the helper function
    if len(lst) == n: # base case is when all items have been processed by helper()
        return lst
    else:
        lst[n] = helper(lst[n]) # passes the specific list item to helper()
        n += 1 # iterates the count
        return doubleStringList(lst, n) # goes to next item in list
    
