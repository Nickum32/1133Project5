# CSci 1133 HW 5
# Nicholas Mayer
# HW Problem A
#
# This program will be used to calculate ln(x) to a desired accuracy
#
def main():
    accuracy = float(input('Enter desired tolerance/accuracy: ')) # get the desired precision from user
    x = float(input('Enter the desired value of x: ')) # get desired value to check
    lnx = 0  # set base value for lnx so program has a value to add in while loop
    comparison = 1000  # this is an arbitrarily high value to start the while loop
    n = 0  # though the series operation starts at n = 1, it's eaier to start at 1 to avoid adding one too many
    while abs(lnx - comparison) > accuracy:  # while loop ends once lnx is within the desired precision
        n += 1
        comparison = lnx  # set comparison to the previous increment's value of lnx
        lnx += ((-1)**(n-1)) * (((x-1)**n) / n)
##        print(lnx)   ### Debug print
    print('The value of ln', x, 'is: ', lnx)
    print('Number of terms used: ', n)
    keepGoing = input('Continue? (Enter Y or y): ')
    if keepGoing in ['Y', 'y']:
        main()
    

if __name__ == '__main__':
    main()
