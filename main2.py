x = 700
y = 700 
d = 2
n = 100
G = 20
dt = 1/500
R = 20

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

    # pyglet.clock.schedule_interval(update, dt)
    # pyglet.app.run()
    sim.run(dt)
    pass