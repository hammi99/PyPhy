import numpy as np

class Simulation():
    
    def __init__(
            masses
            ,positions
            ,velocities
            ,G
            ,dt
    ):
        b = len(positions)
        d = len(positions[0])
        
        self.M   = np.array(masses)
        self.R   = np.array(positions)
        self.dR  = np.array(velocities)
        self.ddR = np.empty([b, d])         # init acceleration
        self.G   = G
        
        self.D = np.empty([b, b, d])        # init displacements
        self.S = np.empty([b, b, d])        # init distances
        
        self.Rb = R[:, np.newaxis]          # init parameters to be used in calculating displacements
        
        
    def step(self, dt):
        
        self.D   = (self.R - self.Rb)                                   # calculating displacements
        self.S   = np.linalg.norm(self.D, axis=2, keepdims=True)        # calculating distance
        self.ddR = self.G * self.M @ np.nan_to_num(self.D / self.S**3)  # calculating acceleration
        
        self.R  += dt * self.dR         # updating positions
        self.dR += dt * self.ddR        # updating velocities