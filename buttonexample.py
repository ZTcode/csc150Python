
from graphics import *

def main():

    win = GraphWin("Button Example", 300, 300)
    box = Rectangle(Point(100, 100), Point(200,200))
    box.draw(win)
    label = Text(Point(150,150), "Quit")
    label.draw(win)
    
    while True:
        p = win.getMouse()
        print(p.getX(), p.getY())
        if 100 < p.getX() < 200 and 100 < p.getY() < 200:
            break
    win.close()
    
main()

                    
                                           
    
