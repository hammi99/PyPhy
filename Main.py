from Classes import *
from Functions import *
from math import *

no_of_bodies = int(input('No of bodies:'))

bodies=[]

for _ in range(no_of_bodies):

    mass = int(input('mass'))
    radius =int(input('radius'))


    position_mag = int(input('pos mag'))
    position_angle = int(input('pos angle'))
    position = Vector(position_mag ,position_angle)

    velocity_mag = int(input('vel mag'))
    velocity_angle = int(input('vel angl'))
    velocity = Vector(velocity_mag ,velocity_angle)

    acceleration_mag = int(input('acc mag'))
    acceleration_angle = int(input('acc angl'))
    acceleration = Vector(acceleration_mag ,acceleration_angle)


    bodies.append(Bodies(mass ,radius ,position ,velocity ,acceleration))

while True:
    for body in bodies:

        body.pos.Update(body.vel)
        body.vel.Update(body.acc)
        #body.acc.Update(Vector(Force/body.mas ,))

    #for body1 in bodies:
     #   for body2 in bodies:

    




