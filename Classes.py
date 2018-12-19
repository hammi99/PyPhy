from math import *
from Functions import *

class Vector:
    def __init__(self ,magnitude ,angle):

        self.comp = ressolve(magnitude ,angle)
        self.angle = angle
        self.magnitude = magnitude


    def Updte(self ,update_vector):

        vector_comp = tuple_add(self.comp ,update_vector.comp)
        mag = magnitude(vector_comp)
        angl = angle(vector_comp)

        self = Vector(mag ,angl)



class Bodies:
    def __init__(self ,mass ,radius ,position ,velocity ,acceleration):

        self.mas = mass
        self.rad = radius

        self.pos = position
        self.vel = velocity
        self.acc = acceleration
        self.mom = Vector(mass*velocity.magnitude ,velocity.angle)