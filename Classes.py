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

    def __init__(self 
                ,mass 
                ,radius 
                ,position 
                ,velocity 
                ,acceleration):

        self.mass         = mass
        self.radius       = radius
        self.position     = position
        self.velocity     = velocity
        self.acceleration = acceleration
        self.momentum     = Vector(mass*velocity.magnitude ,velocity.angle)