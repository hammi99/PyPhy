import pyglet
import numpy as np


class Simulation():
    
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
        
        self.r = np.array(positions,  dtype= float)
        self.b = np.array(bounds)#.reshape([2, 1, d])
        self.v = np.array(velocities, dtype= float)
        self.m = np.array(masses)
        self.R = np.array(radii)
        self.G = np.array(G)

        # n, d = self.r.shape

        # self.a = np.zeros(shape= [n, d])
        # self.d = np.zeros(shape= [n, n, d])
        # self.s = np.zeros(shape= [n, n])

        # self.M = self.G * self.m * self.m[:, None]

        # if self.r.ndim == 2: self.setupDisplay()

        

    def step(self, dt):

        self.r += dt * self.v           # updating positions
        self.v -= dt * self.a           # updating velocities

        # T = (self.m * self.v ** 2).sum() / 2              # total kinetic energy of the system
        # U = H - T                                         # total potential energy of the system
        #                                                     ma = dU/dv ???

        # t0, t1 = self.t

        # d = self.r[t0] - self.r[t1]                                         # calculating displacements
        # s = np.linalg.norm(d, axis= -1)                                     # calculating distances

        # self.d[t0, t1] , self.d[t1, t0] = d, -d                             # assigning displacements           shape= [n, n, d]
        # self.s[t0, t1] = self.s[t1, t0] = s                                 # assigning distances               shape= [n, n]

        # self.d = self.r - self.r[:, None]
        # self.s = (self.d**2).sum(axis= -1)
        
        # self.a = self.G * self.M @ np.nan_to_num(self.d.T / self.s**3)      # calculating acceleration          shape= [d, n]
        # self.a = self.a.T

        

    def checkBounds(self):

        mask = np.where(self.r < self.b[0])
        self.v[mask] *= -1
        self.r[mask] = self.b[0][mask[1]];

        mask = np.where(self.r > self.b[1])
        self.v[mask] *= -1
        self.r[mask] = self.b[1][mask[1]];



        



    def checkCollission(self, dt):

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

        self.window = pyglet.window.Window(*self.b[1][0])

        p = self.r.ravel()
        n = len(p)//2

        batch = pyglet.graphics.Batch()
        vertex_list = batch.add(
            n, 
            pyglet.gl.GL_POINTS,
            None,
            ('v2f', p)
        )
        vertex_list.vertices = p
        pass



if __name__ == "__main__":

    b = 100
    d = 2
    G = 10
    bounds = 100

    sim = Simulation(
        masses     = np.random.normal([b]) * 100,
        positions  = np.random.normal([b, d]) * 100 + 350,
        velocities = np.random.normal([b, d]) * 50 - 25,
        G          = G,
        bounds     = bounds,
        radii      = 0,
    )

    sim.step(dt)
    quit()