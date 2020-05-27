import numpy as np

class Simulation():
    
    def __init__(
            self
            ,masses
            ,positions
            ,velocities
            ,G
            ,bounds
            ,radii
    ):
        b = len(positions)
        d = len(positions[0])
        
        self.m = np.array(masses)
        self.r = np.array(positions)
        self.v = np.array(velocities)
        self.B = np.array(bounds)
        self.R = np.array(radii)
        self.G = np.array(G)
        
        self.rb = self.r[:, np.newaxis]             # init parameter to be used in calculating displacements
        #self.Rb = self.R + self.R[:, np.newaxis]    # sum of radii of every possible pair
        #self.Rb = self.Rb[..., np.newaxis]
        
        self.bounds = np.array(bounds)

    def step(self, dt):
        
        self.d = self.r - self.rb                                     # calculating displacements       shape= (b, b, d)
        self.s = np.linalg.norm(self.d, axis=2, keepdims=True)        # calculating distance "2-norm"   shape= (b, b, 1)
        self.a = self.G * self.m @ np.nan_to_num(self.d / self.s**3)  # calculating acceleration        shape= (b, b, d)

        self.r += dt * self.v        # updating positions
        self.v += dt * self.a        # updating velocities

    def check_bounds(self):

        filter = (self.r > self.bounds) | (self.r < 0)
        self.v[filter] = -self.v[filter]

    def check_colission():

        filter = self.s < self.Rb
        pass
