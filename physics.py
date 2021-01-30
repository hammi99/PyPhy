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

        a = self.r + self.R
        b = self.r - self.R

        mask = True

        for p in self.r.T:
            i = p.argsort()
            j = i.argsort()

            b[i][:-1] < a[i][1:]

        self.r.argsort()

        # filter = (self.s < self.Rb) & (self.s > 0)                                                # shape= [b, b]
        # filter2 = np.where(filter)  # [2, n]

        # mass_ratios = self.Mb[filter]                                                         # shape= [n]
        # del_v       = self.v[:, filter2[0]] - self.v[:, filter2[1]]
        # del_r       = self.d[:, filter]
        # v_dot_r     = np.einsum('ij,ij->j', del_v, del_r)      # shape= [n]
        # del_vr_hat  = np.nan_to_num(
        #       v_dot_r \
        #     / self.s[filter]**2
        # )                                                                           # shape= [d, n]
        
        # #self.r[:, filter2[0]] -= dt * self.v[:, filter2[0]]
        # self.v[:, filter2[0]] -= (mass_ratios * del_v * del_vr_hat)


    def setupDisplay(self):

        m = 20
        n = self.r.shape[0]

        x = np.linspace(0, 2*np.pi, num= m)

        circumfrence = np.array([
            np.cos(x),
            np.sin(x),

        ]).T * self.R[..., None]

        batch = pyglet.graphics.Batch()
        vertex_list = batch.add(
            n * m, 
            # pyglet.gl.GL_LINES,
            pyglet.gl.GL_LINES,
            None,
            'v2f',
        )

        window = pyglet.window.Window(*self.b[1], resizable= True)

        @window.event
        def on_draw():

            p = self.r[:, None] + circumfrence

            vertex_list.vertices = p.ravel()
            window.clear()
            batch.draw()


    def run(self, dt):

        def foo(dt):
            self.step(dt)
            # self.checkBounds()
            # self.checkCollission()

            os.system('clear')
            print(f'fps: {pyglet.clock.get_fps()}')


        pyglet.clock.schedule_interval(foo, dt)
        pyglet.app.run()
        





x = 700
y = 700 
d = 2
n = 1000
G = 20
dt = 1/500
R = 1

bounds = [
    [0, 0], 
    [x, y],
]

sim = Simulation(
    masses     =  np.random.random([n]) * 100,
    radii      =  R,
    positions  =  np.random.random([n, d]) * 100 + 350,
    velocities =  np.random.normal(0, 100, [n, d]),
    G          =  G,
    bounds     =  bounds
)


if __name__ == '__main__':

    sim.run(dt)
    pass