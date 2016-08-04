#
# Implement a function that takes as input three variables, and returns the largest of the three.
#  Do this without using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally
#  takes care of for us. All you need is some variables and if statements!

def maxVar(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

maxVar(5,10,15)
