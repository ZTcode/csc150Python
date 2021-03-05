#button.py
from graphics import *

class Button:

    """A buttom is a labeled rectangle in a window.
    it is activated ofr deactivated with the active() and devactivate methods.
    The clicked(p) method returns true if the button is active and p is inside it"""
    
    def __init__(self, win, center, width, height, label):
        """creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, "Quit")"""

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('')
        self.rect.setOutline('')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate
        
        

    def clicked(self, p):
        "returns true if button active and p is inside"
        return(self.activate and
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button"
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(1)
        self.activate = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('blue')
        self.rect.setWidth(1)
        self.activate = False


    
