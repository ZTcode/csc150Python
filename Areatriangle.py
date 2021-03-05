#triangleArea.py
# This program gets length of 3 sides of a triangle from the user and computes
# the area of a triangle

import math

def main():
    a, b, c = eval(input("Enter length of three sides seperated by a comma: "))

    s = (a + b + c)/2
    z = s*(s-a)*(s-b)*(s-c)
    if z > 0:
        area = math.sqrt(z)
        print("The area of the triangle is", area)
    else:
        print("There is no triangle with these sides.")

        
main()


    
