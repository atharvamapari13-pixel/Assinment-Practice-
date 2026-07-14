# This is Q3.py in the 'Assignment 26' folder.
class Arithmatic:
    def __init__(self):
        self.value1=0
        self.value2=0
    def Accept(self):
        try:
            self.value1=int(input("Enter the Value 1:"))
            self.value2=int(input("Enter the Value 2:"))
        except Exception as e:
            print("Enter the Valid Number...",e)
    def Addition(self):
        return self.value1 + self.value2
    def Sub(self):
        return self.value1 - self.value2
    def Multiple(self):
        return self.value1 * self.value2
    def Division(self):
        try:
            return self.value1 / self.value2
        except Exception as z:
            print("Exception is There:",z)
obj1=Arithmatic()
obj2=Arithmatic()
obj1.Accept()
Ret = obj1.Addition()
Ret1 = obj1.Multiple()
print("Addition is:",Ret)
print("Multiple is:",Ret1)

obj2.Accept()
Ret2 = obj2.Division()
Ret3 = obj2.Multiple()
print("Division is:",Ret2)
print("Multiple is:",Ret3)




    
    
