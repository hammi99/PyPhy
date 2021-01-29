p = sim.r.ravel()
n = len(p)//2

batch = pyglet.graphics.Batch()
vertex_list = batch.add(
    n, 
    pyglet.gl.GL_POINTS,
    None,
    ('v2f', p)
)
vertex_list.vertices = p