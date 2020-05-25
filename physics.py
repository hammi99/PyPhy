import numpy as np

class Simulation():
    
    def __init__(
            self
            ,masses
            ,positions
            ,velocities
            ,G
    ):
        b = len(positions)
        d = len(positions[0])
        
        self.m = np.array(masses)
        self.r = np.array(positions)
        self.v = np.array(velocities)
        self.a = np.empty([b, d])       # init acceleration
        self.G = G
        
        self.d = np.empty([b, b, d])    # init displacements
        self.s = np.empty([b, b, d])    # init distances
        
        self.rb = self.r[:, np.newaxis] # init parameters to be used in calculating displacements
        
        
    def step(self, dt):
        
        self.d = (self.r - self.rb)                                   # calculating displacements
        self.s = np.linalg.norm(self.d, axis=2, keepdims=True)        # calculating distance
        self.a = self.G * self.m @ np.nan_to_num(self.d / self.s**3)  # calculating acceleration
        
        self.r += dt * self.v        # updating positions
        self.v += dt * self.a        # updating velocities
