import os
import pyglet
import numpy as np


class Simulation:
    
    def __init__(
            self,
            masses      = np.random.normal( 50, 100, size= [100]),
            radii       = np.random.normal(  1,   1, size= [1]),
            positions   = np.random.normal( 50, 100, size= [100, 2]),
            velocities  = np.random.normal(350, 100, size= [100, 2]),
            G           = np.random.normal(  1,   1, size= [1]),
            # bounds      = np.array([[]])
            bounds      = np.array([500, 500])
        ):
        
        self.m = np.array(masses)
        self.r = np.array(positions,  dtype= float)
        self.v = np.array(velocities, dtype= float)
        self.R = np.array(radii)
        self.b = np.array(bounds)
        self.G = np.array(G)

        self.a = np.zeros_like(self.r)

        self.setupDisplay()


    def step(self, dt):

        self.r += dt * self.v           # updating positions
        self.v -= dt * self.a           # updating velocities


        # T = (self.m * self.v ** 2).sum() / 2              # total kinetic energy of the system
        # U = H - T                                         # total potential energy of the system
        #                                                     ma = dU/dv ???

        
    def checkBounds(self):

        temp = self.b[0] + self.R
        mask = np.where(self.r < temp)
        self.v[mask] *= -1
        self.r[mask] = temp[..., mask[1]]       # not applicapable for n different radii

        temp = self.b[1] - self.R
        mask = np.where(self.r > temp)
        self.v[mask] *= -1
        self.r[mask] = temp[..., mask[1]]       # not applicapable for n different radii


    def checkCollission(self):

        # use sweep and pruning algorithm in the future

        d = self.r - self.r[:, None]
        d = np.linalg.norm(d, axis= -1)

        mask = d < (self.R + self.R[..., None])
        np.fill_diagonal(mask, False)
        m, _ = np.where(mask)

        self.colours[:] = 255
        self.colours[m] = np.array([255, 0, 0])

        del_v = self.v - self.v[:, None]
        del_r = self.r - self.r[:, None]

        M = 2 * self.m / (self.m + self.m[..., None])

        tmp = M                                 \
            * (del_v * del_r).sum(axis= -1)     \
            / (del_r ** 2   ).sum(axis= -1)        
        tmp = tmp[..., None]                    \
            * del_r

        tmp[~mask] = 0

        # increases total energy of the system for some reason
        # suspected reason: after collision (boundry overlap)
        # positions are not updated to eliminate boundry overlap
        # only velocities are updated so a single collision might 
        # be interpreted as multiple collisions causing velocity 
        # updates again and again
        # or maybe, in the elastic collision equation, we are 
        # using the distance between the centeres of the bodies 
        # which may or may not be smaller than the sum or their 
        # radii. in the real world difference b/w positions is 
        # equal to the sum of radii for colliding bodies

        # self.v[m] -= tmp[mask]


    def setupDisplay(self):

        m = 150
        n = self.r.shape[0]

        self.colours = np.full(shape= [n, m, 3], fill_value= 255)

        x = np.linspace(0, 2*np.pi, num= m)
        circumfrence = np.array([
            np.cos(x),
            np.sin(x),

        ]).T * self.R[..., None]

        batch = pyglet.graphics.Batch()
        vertex_list = batch.add(
            n * m, 
            # pyglet.gl.GL_LINES,
            pyglet.gl.GL_POINTS,
            None,
            'v2f',
            'c3B',
        )

        window = pyglet.window.Window(*self.b[1], resizable= True)

        @window.event
        def on_draw():

            p = self.r[:, None] + circumfrence
            c = self.colours

            vertex_list.vertices = p.ravel()
            vertex_list.colors   = c.ravel()

            window.clear()
            batch.draw()


    def status(self):

        U = 0

        T = self.m                      \
          * (self.v ** 2).sum(axis= -1) \
        
        T = T.sum()

        H = U + T

        r  = ''
        r += 'energies:\n'
        r += f'\tTotal    : {H}\n'
        r += f'\tKinetic  : {U}\n'
        r += f'\tPotential: {T}\n'

        print(r)


    def run(self, dt):

        def foo(dt):

            os.system('clear')
            print(f'fps: {pyglet.clock.get_fps()}')

            self.step(dt)
            self.checkBounds()
            self.checkCollission()

            self.status()


        pyglet.clock.schedule_interval(foo, dt)
        pyglet.app.run()
        





x = 700
y = 700 
d = 2
n = 10
G = 20
dt = 1/500
R = 10

bounds = [
    [0, 0], 
    [x, y],
]

sim = Simulation(
    masses     =  np.random.random([n]) * 100,
    radii      =  R,
    positions  =  np.random.random([n, d]) * 300 + 350,
    velocities =  np.random.normal(0, 100, [n, d]),
    G          =  G,
    bounds     =  bounds
)


if __name__ == '__main__':

    sim.run(dt)
    pass