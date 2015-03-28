import OpenGL.GL as gl
import OpenGL.GLUT as glut
import sys

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(-0.95,-0.95)
    gl.glVertex2f(0.95,-0.95)
    gl.glVertex2f(0,0.95)
    gl.glEnd()
    gl.glFlush()

def reshape(width,height):
    gl.glViewport(0, 0, width, height)

def keyboard( key, x, y ):
    if key == '\033':
        sys.exit( )

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_RGBA)
glut.glutCreateWindow('Hello world!')
glut.glutReshapeWindow(512,512)
glut.glutReshapeFunc(reshape)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()

