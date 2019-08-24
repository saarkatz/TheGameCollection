"""
This module is a sample of OpenGL code.
"""
import OpenGL
from OpenGL.GL import glClear, glLoadIdentity, glBegin, glVertex2f, glEnd, \
    glColor3f, glViewport, glMatrixMode, glOrtho, \
    GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_QUADS, \
    GL_MODELVIEW, GL_PROJECTION
import OpenGL.GLU
from OpenGL.GLUT import glutInit, glutInitDisplayMode, glutInitWindowSize, \
    glutInitWindowPosition, glutCreateWindow, glutDisplayFunc, glutIdleFunc, \
    glutMainLoop, glutSwapBuffers, GLUT_RGBA

w, h = 500, 500


# ---Section 1---
def square():
    # We have to declare the points in this sequence: bottom left,
    # bottom right, top right, top left
    glBegin(GL_QUADS)  # Begin the sketch
    glVertex2f(100, 100)  # Coordinates for the bottom left point
    glVertex2f(200, 100)  # Coordinates for the bottom right point
    glVertex2f(200, 200)  # Coordinates for the top right point
    glVertex2f(100, 200)  # Coordinates for the top left point
    glEnd()  # Mark the end of drawing


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# ---Section 2---


def showScreen():
    # Remove everything from screen (i.e. displays all white)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0)  # Set the color to pink
    square()  # Draw a square using our function
    glutSwapBuffers()


# ---Section 3---

# Initialize a glut instance which will allow us to customize our
# window
glutInit()
# Set the display mode to be colored
glutInitDisplayMode(GLUT_RGBA)
# Set the width and height of your window
glutInitWindowSize(500, 500)
# Set the position at which this windows should appear
glutInitWindowPosition(0, 0)
# Give your window a title
wind = glutCreateWindow("OpenGL Coding Practice")
# Tell OpenGL to call the showScreen method continuously
glutDisplayFunc(showScreen)
# Draw any graphics or shapes in the showScreen function at all times
glutIdleFunc(showScreen)
# Keeps the window created above displaying/running in a loop
glutMainLoop()
