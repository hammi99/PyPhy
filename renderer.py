import pyglet

class Renderer():

    def __init__(self): 

        self.window = pyglet.window.Window(resizable= True)

        self.batch = pyglet.graphics.Batch()
        vertex_list = batch.add(
            n * m, 
            pyglet.gl.GL_LINES,
            None,
            'v2f',
        )


