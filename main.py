import os
import pyglet
import physics
import numpy as np

# bla bla bla

clear = lambda: os.system('clear')

x = 800
y = 800 
d = 2
n = 100
G = 20
dt = 1/500

bounds = [
    [0, 0], 
    [x, y],
]

sim = physics.Simulation(
    masses     =  np.random.random([n]) * 100,
    radii      =  10,
    positions  =  np.random.random([n, d]) * 100 + 350,
    velocities =  np.random.normal(0, 100, [n, d]),
    G          =  G,
    bounds     =  bounds
)

window = pyglet.window.Window(x, y)
p = sim.r.ravel()
n = len(p)//2

batch = pyglet.graphics.Batch()
vertex_list = batch.add(
    n, 
    pyglet.gl.GL_POINTS,
    None,
    # ('v2f', p)
    'v2f'
)
# vertex_list.vertices = p

def update(dt):
    global sim
    
    sim.step(dt)
    sim.checkBounds()
    #sim.check_collission(dt)
    clear()
    print(f'fps: {pyglet.clock.get_fps()}')



@window.event
def on_draw():

    window.clear()
    vertex_list.vertices = sim.r.ravel()
    batch.draw()
    

if __name__ == '__main__':

    pyglet.clock.schedule_interval(update, dt)
    pyglet.app.run()