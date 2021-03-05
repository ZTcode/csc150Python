import math 
class Sphere:
    #define a constructor of sphere
    #constructor is a special function that is used to intialize an object
    #of this Sphere class
    def __init__(self, radius):
        #to initialize this sphere object properly we need to
        #remember the radius
        #if we try to assign some variable here, python regards them as
        #local variables, which dissapper after the function ends
        theRadius = radius
        #To keep the information we create an 'instance variable' through
        #the self parameter.
        self.radius = radius

    def volume(self):  #we always need to provide self parameter
        #we have the radius of this sphere as self.radius
        vol = 4.0/3.0 * math.pi * self.radius ** 3
        return vol
    def surfaceArea(self):
        sa = 4.0 * math.pi * self.radius **2
        return sa


    def getRadius(self):
        return self.radius



    
def main():
    mySphere = Sphere(100) #100 is passed to the constructor as radius
    print("The volume of this sphere is", mySphere.volume())
    print("The surface area of this sphere is", mySphere.surfaceArea())
    print("The radius of the sphere is", mySphere.getRadius())
    

main()
        
        
