## Sean Bloomsburg
## sbloomsburg@gmail.com
##
## This module is essentially the implementation of the first function
## described in the explanation. It finds the quotient between two
## movies.
##


from math import *


def find_similarity(user_vector, rated_item_vector):
    dot = 0.0
    a = 0.0
    b = 0.0
    for i in range(20):
        dot = dot + (float(user_vector[i]) * float(rated_item_vector[i]))

    for i in range(20):
        a = a + (user_vector[i] ** 2)
    A = abs(sqrt(float(a)))

    for i in range(20):
        b = b + (float(rated_item_vector[i]) ** 2)
    B = abs(sqrt(float(b)))
    denominator = A * B

    if denominator != 0:
        quotient = dot / denominator
    else:
        print "Division by Zero Error"
        print "Dot Product was ", dot
        quotient = 0.0

    theta = acos(quotient)

    return theta


if __name__ == find_similarity:
    find_similarity
