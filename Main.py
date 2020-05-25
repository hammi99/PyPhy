from Classes import *
from Functions import *
from math import *

no_of_bodies = int(input('No of bodies: '))

bodies = []

for _ in range(no_of_bodies):
    n = _ + 1
    print("\nInputing values of Body {}".format(n))
    mass = int(input('mass_{}:\t\t'.format(n)))
    radius = int(input('radius_{}:\t'.format(n)))

    position_mag = int(input('pos mag_{}:\t'.format(n)))
    position_angle = int(input('pos angle_{}:\t'.format(n)))
    position = Vector(position_mag, position_angle)

    velocity_mag = int(input('vel mag_{}:\t'.format(n)))
    velocity_angle = int(input('vel angl_{}:\t'.format(n)))
    velocity = Vector(velocity_mag, velocity_angle)

    acceleration_mag = int(input('acc mag_{}:\t'.format(n)))
    acceleration_angle = int(input('acc angl_{}:\t'.format(n)))
    acceleration = Vector(acceleration_mag, acceleration_angle)
    bodies.append(Bodies(mass, radius, position, velocity, acceleration))

while True:
    for body in bodies:

        body.pos.Update(body.vel)
        body.vel.Update(body.acc)
        #body.acc.Update(Vector(Force/body.mas ,))

    # for body1 in bodies:
     #   for body2 in bodies:
