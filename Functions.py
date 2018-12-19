from math import *

def tuple_add(*tuples):
    tuple_sum = ()
    for x in range(len(tuples[0])):
        total = 0
        for y in tuples:
            total = total + y[x]
        tuple_sum = tuple_sum + (total,)

    return tuple_sum

def tuple_neg(tuple):
    negative_tuple = ()
    for component in tuple:
        negative = negative_tuple + (-1 * component,)

    return negative_tuple

def tuple_multi(scalar ,tuple):
    tuple_product = ()
    for component in tuple:
        tuple_product = tuple_product + component*scalar

    return tuple_product

def magnitude(tuple):
    mag_sq = 0
    for x in tuple:
        mag_sq = mag_sq + x**2

    return sqrt(mag_sq)



def angle(tuple):
    theta = atan2(tuple[1] ,tuple[2])

    return theta

def ressolve(magnitude ,angle):
    a = (magnitude*cos(angle) ,magnitude*sin(angle))

    return a