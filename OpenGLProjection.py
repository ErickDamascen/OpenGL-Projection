from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 

speed = 0.01 #speed of rotation
ratio = 1 
distance = -12 #distance of observator

#rotation
X_AXIS = 1
Y_AXIS = 1
Z_AXIS = 1

def clearScreen():
    
    global ratio, distance

    glClearColor(0, 0, 0, 0)
    glClearDepth(1)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    

    glOrtho(-5*ratio,5*ratio,-5*ratio,5*ratio,-100,100) #ignore distance of objects and show orthogonal form
    #gluPerspective(45, float(800)/float(600), 0.1, 100) #show perspective form
    #glFrustum(-1,1,-1,1,1,100) #describes a perspective matrix that produces a perspective projection
    

    
    glMatrixMode(GL_MODELVIEW)

def cube():
    glBegin(GL_QUADS)
    #Quad 1
    glColor(1,0,0,0)
    glVertex3f( 1., 1., 1.)  
    glVertex3f( 1.,-1., 1.)  
    glVertex3f( 1.,-1.,-1.)   
    glVertex3f( 1., 1.,-1.)  
    #Quad 2
    glColor(0,1,0,0)
    glVertex3f( 1., 1.,-1.)   
    glVertex3f( 1.,-1.,-1.)  
    glVertex3f(-1.,-1.,-1.)   
    glVertex3f(-1., 1.,-1.)  
    #Quad 3
    glColor(0,0,1,0)
    glVertex3f(-1., 1.,-1.)  
    glVertex3f(-1.,-1.,-1.)   
    glVertex3f(-1.,-1., 1.)   
    glVertex3f(-1., 1., 1.)   
    #Quad 4
    glColor(1,1,1,0)
    glVertex3f(-1., 1., 1.)   
    glVertex3f(-1.,-1., 1.)  
    glVertex3f( 1.,-1., 1.)   
    glVertex3f( 1., 1., 1.)   
    #Quad 5
    glColor(1,1,0,0)
    glVertex3f(-1., 1.,-1.)   
    glVertex3f(-1., 1., 1.)   
    glVertex3f( 1., 1., 1.)   
    glVertex3f( 1., 1.,-1.)   
    #Quad 6
    glColor(0,1,1,0)
    glVertex3f(-1.,-1., 1.)   
    glVertex3f(-1.,-1.,-1.)   
    glVertex3f( 1.,-1.,-1.)   
    glVertex3f( 1.,-1., 1.)  
    glEnd()

def pyramid():
    glBegin(GL_TRIANGLES)
    #Triangle 1
    glColor(1,0,0,0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    #Triangle 2
    glColor(1,0,1,0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    #Triangle 3
    glColor(0,1,0,0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    #Triangle 4
    glColor(0,0,1,0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glEnd()
    #Quad
    glBegin(GL_QUADS)
    glColor(0,1,1,0)
    glVertex3f(-1.,-1., 1.)   
    glVertex3f(-1.,-1.,-1.)   
    glVertex3f( 1.,-1.,-1.)   
    glVertex3f( 1.,-1., 1.)   
    glEnd()

def hourglass():
    glBegin(GL_TRIANGLES)

    #Triangle 1
    glColor(1,0,0,0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    #Triangle 2
    glColor(1,1,1,0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    #Triangle 3
    glColor(0,1,0,0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    #Triangle 4
    glColor(0,0,1,0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glEnd()
    #Quad
    glBegin(GL_QUADS)
    glColor(0,1,1,0)
    glVertex3f(-1.,-1., 1.)   
    glVertex3f(-1.,-1.,-1.)   
    glVertex3f( 1.,-1.,-1.)  
    glVertex3f( 1.,-1., 1.)   
    glEnd()

    glBegin(GL_TRIANGLES)
    #Triangle 1
    glColor(1,0,0,0)
    glVertex3f( 0.0,-1.0, 0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    #Triangle 2
    glColor(1,1,1,0)
    glVertex3f( 0.0,-1.0, 0.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    #Triangle 3
    glColor(0,1,0,0)
    glVertex3f( 0.0,-1.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    #Triangle 4
    glColor(0,0,1,0)
    glVertex3f( 0.0,-1.0, 0.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glEnd()
    #Quad
    glBegin(GL_QUADS)
    glColor(0,1,1,0)
    glVertex3f( 1., 1.,-1.)   
    glVertex3f( 1., 1., 1.)  
    glVertex3f(-1., 1., 1.)   
    glVertex3f(-1., 1.,-1.)   
    glEnd()

def scene():
    
    global X_AXIS, Y_AXIS, Z_AXIS, speed, distance
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    glTranslatef(0, 0, distance) #position in the screen
    glRotatef(X_AXIS,1,1,0)
    glRotatef(Y_AXIS,0,1,0)
    glRotatef(Z_AXIS,0,0,1)
    cube()

    glLoadIdentity()
    glTranslatef(0, 3, distance-5)  #position in the screen
    glRotatef(X_AXIS,1,1,0)
    glRotatef(Y_AXIS,0,1,0)
    glRotatef(Z_AXIS,0,0,1)
    pyramid()

    glLoadIdentity()
    glTranslatef(0, -3, distance+2)  #position in the screen
    glRotatef(X_AXIS,1,1,0)
    glRotatef(Y_AXIS,0,1,0)
    glRotatef(Z_AXIS,0,0,1)
    hourglass()

    X_AXIS = X_AXIS - speed
    Y_AXIS = Y_AXIS - speed
    Z_AXIS = Z_AXIS - speed

    glutSwapBuffers()

if __name__ == "__main__":

    glutInit()   

    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Scene OpenGL")
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(50, 50)

    glutDisplayFunc(scene)
    glutIdleFunc(scene)
    
    clearScreen()
    glutMainLoop()