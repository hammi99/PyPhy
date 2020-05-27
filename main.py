import pyglet
import physics
import numpy as np

x = 800
y = 800 
b = 100
d = 2
G = 5
dt = 1/200
bounds = [x, y]

sim = physics.Simulation(
     masses     =  np.random.random([b]) * 100
    ,positions  =  np.random.random([b, d]) * 100 + 350
    ,velocities = (np.random.random([b, d]) - 0.5) * 50
    ,G          =  G
    ,bounds     = bounds
    ,radii      = 0
)

window = pyglet.window.Window(x, y)
p = sim.r.ravel()
n = sim.r.shape[0]


def update(dt):
    global sim
    sim.step(dt)
    sim.check_bounds()
    fps = pyglet.clock.get_fps()
    print(fps)


@window.event
def on_draw():

    window.clear()
    pyglet.graphics.draw(n, pyglet.gl.GL_POINTS
        ,('v2f', p)
    )

if __name__ == '__main__':

    pyglet.clock.schedule_interval(update, dt)
    pyglet.app.run()
