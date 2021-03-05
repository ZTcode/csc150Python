# anonymizerG.py
# this program anonymize a photo by painting cartoon pictures on top of faces.

from graphics import *
import math

def drawFace(center, size, win):
    x = center.getX()
    y = center.getY()
    face = Circle(center, size)
    face.setFill("brown")
    face.draw(win)
    
    e1 = Circle(Point(x-size*0.6, y-size*0.5), 5)
    e1.setFill("blue")
    e1.draw(win)
    e2 = Circle(Point(x+size*.06, y-size*.05), 5)
    e2.setFill("blue")
    e2.draw(win)
    mouth = Circle(Point(x, y+size/2), size/3)
    mouth.setFill("red")
    mouth.draw(win)
    nose = Circle(Point(x, y), size/2)
    nose.setFill("orange")
    nose.draw(win)
    
def main():
    filename = input("Enter the name of an image file: ")
    nFaces = eval(input("How many faces in the image? "))
    im = Image(Point(0,0), filename)

    win = GraphWin("Anonymizer", im.getWidth(), im.getHeight())
    im.move(im.getWidth()/2, im.getHeight()/2) #move it to the center
    im.draw(win)

    for i in range(nFaces):
        center = win.getMouse()
        edge = win.getMouse()
        dx = center.getX() - edge.getX()
        dy = center.getY() - edge.getY()
        distance = math.sqrt(dx*dx + dy*dy)
        drawFace(center, distance, win)

main()
