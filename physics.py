import numpy as np


class Simulation():
    
    def __init__(
            self,
            masses,
            radii,
            positions,
            velocities,
            G,
            bounds
    ):
        
        self.b = np.array(bounds)
        self.r = np.array(positions,  dtype= float)
        self.v = np.array(velocities, dtype= float)
        self.M = np.array(masses)
        self.R = np.array(radii)
        self.G = np.array(G)

        n, d = self.r.shape

        self.d = np.zeros([n, n, d])
        self.s = np.zeros([n, n])

        self.t = np.triu_indices(n, k= 1)

        self.ceil  = self.b[0] - self.R
        self.floor = self.b[1] + self.R
        
        #self.Mb = 2 * self.M / (self.M + self.M[..., np.newaxis])
        #self.Rb = self.R + self.R[..., np.newaxis]    # sum of radii of every possible pair
        

    def step(self, dt):

        t0, t1 = self.t

        d = self.r[t0] - self.r[t1]                                         # calculating displacements
        s = np.linalg.norm(d, axis= -1)                                     # calculating distances

        self.d[t0, t1] , self.d[t1, t0] = d, -d                             # assigning displacements           shape= [n, n, d]
        self.s[t0, t1] = self.s[t1, t0] = s                                 # assigning distances               shape= [n, n]

        self.a = self.G * self.M @ np.nan_to_num(self.d.T / self.s**3)      # calculating acceleration          shape= [d, n]

        self.r += dt * self.v                                               # updating positions
        self.v += dt * self.a.T                                             # updating velocities


    def check_bounds(self):

        mask = np.where(self.ceil < self.r)
        
        self.v[mask] = -self.v[mask]
        self.r[mask] =  self.ceil[mask[1]]
               
        mask = np.where(self.r < self.floor)
        
        self.v[mask] = -self.v[mask]
        self.r[mask] =  self.floor[mask[1]]


    def check_collission(self, dt):

        filter = (self.s < self.Rb) & (self.s > 0)                                                # shape= [b, b]
        filter2 = np.where(filter)  # [2, n]

        mass_ratios = self.Mb[filter]                                                         # shape= [n]
        del_v       = self.v[:, filter2[0]] - self.v[:, filter2[1]]
        del_r       = self.d[:, filter]
        v_dot_r     = np.einsum('ij,ij->j', del_v, del_r)      # shape= [n]
        del_vr_hat  = np.nan_to_num(
              v_dot_r \
            / self.s[filter]**2
        )                                                                           # shape= [d, n]
        
        #self.r[:, filter2[0]] -= dt * self.v[:, filter2[0]]
        self.v[:, filter2[0]] -= (mass_ratios * del_v * del_vr_hat)



if __name__ == "__main__":

    b = 100
    d = 2

    sim = Simulation(
        masses     =  np.random.random([b]) * 100,
        positions  =  np.random.random([b, d]) * 100 + 350,
        velocities = (np.random.random([b, d]) - 0.5) * 50,
        G          =  G,
        bounds     = bounds,
        radii      = 0,
    )

    sim.step(dt)
    quit()