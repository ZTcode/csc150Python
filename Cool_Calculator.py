# Cool_Calculator.py

from graphics import *

def main():
    win = GraphWin("Cool Calculator", 300, 300)
    

    win.setCoords(0, 6, 6, 0)
    win.setBackground("blue")

    label1 = Text(Point(3, .75), "Cool Calculator v4.20")
    label1.setFill("green")
    label1.draw(win)
    label1.setSize(30)

    label2 = Text(Point(3, 1.5), "Enter a mathmatical expression:")
    label2.draw(win)
    label2.setSize(15)
    entry = Entry(Point(3, 2.25), 15)
    entry.draw(win)
    

    button = Rectangle(Point(2, 2.75), Point(4, 4))
    button.setFill("orange")
    button.draw(win)
    label3 = Text(Point(3, 3.4), "Evaluate")
    label3.setFill("black")
    label3.draw(win)

    label4 = Text(Point(2, 5), "The Expression evaluates to:")
    label4.draw(win)
    label4.setSize(14)
    box = Rectangle(Point(4, 4.5), Point(5.3, 5.5))
    box.setFill("purple")
    box.draw(win)
    
    win.getMouse()

    equation = eval(entry.getText())
    label5 = Text(Point(4.5, 5), equation)
    label5.draw(win)

    label3.setText("Quit")
    label3.setFill("green")
    button.setFill("red")
    win.getMouse()
    win.close()
    
    

    


main()
