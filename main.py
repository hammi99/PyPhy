import pyglet
import physics
import numpy as np

b = 100
d = 2
G = 5
dt = 1/120

sim = physics.Simulation(
    np.random.random([b]) * 100
    ,np.random.random([b, d]) * 100 + 400
    ,np.zeros([b, d])
    #,np.random.random([m, 2])
    ,G
)

window = pyglet.window.Window(800, 800)
p = sim.r.ravel()
n = sim.r.shape[0]

def update(dt):
    global sim
    sim.step(dt)


@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(n, pyglet.gl.GL_POINTS
        ,('v2f', p)
    )

if __name__ == '__main__':

    pyglet.clock.schedule_interval(update, dt)
    pyglet.app.run()