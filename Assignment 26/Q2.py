# This is Q2.py in the 'Assignment 26' folder.
class circle:
    def __init__(self):
        self.Area = 0
        self.Cir = 0
        self.radius = 0
    def Accept(self):
        self.radius = int(input("Enter the radius:"))
    def CalculateArea(self):
        self.Area = 3.14 * self.radius * self.radius   
    def CalculateCircumference(self):
        self.Cir =  2*(3.14 * self.radius)
        #print("Circumference of the Circle is:",self.Cir)
    def Display(self):
        print("Radius of the  Circle is : ",self.radius)
        print("Circumference of the Circle is:",self.Cir)
        print("Area of the Circle is:",self.Area)
obj=circle()
obj.Accept()
obj.CalculateCircumference()
obj.CalculateArea()
obj.Display()



