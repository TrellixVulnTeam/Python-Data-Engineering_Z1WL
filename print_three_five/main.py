# -*- coding: utf-8 -*-

def is_multiple_of_x(n, x):
    """To find if n is multiple of x."""
    return n % x == 0


def print_numbers(n):
    """Return numbers from 1 to n, with below changes :
    If n is multiple of 3: Print "Three"
    If n is multiples of 5: Print "Five"
    If n is multiples of 3 and 5: Print "ThreeFive"
    if not above same numeric value
    """

    if n >=1 and n <=100:
        if is_multiple_of_x(n, 3) and is_multiple_of_x(n, 5):
            result='ThreeFive'
        elif is_multiple_of_x(n, 3):
            result = 'Three'
        elif is_multiple_of_x(n, 5):
            result = 'Five'
        else:
            result = str(n)
        return result
    else:
        print(n)
        return 'Value out of bound!!' 


if __name__ == "__main__":
    n = 100
    #Loop through from 1 to 100 to print expected result
    for i in range(1,n+1):
        print(print_numbers(i))
        