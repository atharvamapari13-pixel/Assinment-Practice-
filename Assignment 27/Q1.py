# This is Q1.py in the 'Assignment 27' folder.
class Bookstore:
    No_Books = 0
    def __init__(self,Name, Author):
        self.Name = Name
        self.Author =  Author
        Bookstore.No_Books +=  1
    def Display(self):
        print(f"{self.Name} By {self.Author} Number of Book: {self.No_Books}")
obj1 = Bookstore("C", "Atharva")
obj2 = Bookstore("C++", "Atharva Mapari")
obj1.Display()
obj2.Display()

