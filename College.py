class Person:

    Total_per = 0

    def __init__(self, Name, Age, ID):
        self.name = Name
        self.age = Age
        self.id = ID
        Person.Total_per += 1

    def Accept(self):
        try:
            self.name = input("Enter the name:")
            self.age = int(input("Enter the Age:"))
            if self.age>= 18 and self.age<=100:
                pass
            else:
                print("Enter the Valid Age")
            self.id = int(input("Enter the ID:"))
        except Exception as e:
            print("Exception is",e)

    def Display(self):
        print("name:",self.name)
        print("Age:",self.age)
        print("ID:",self.id)

class Student(Person):

    def __init__(self, Name, Age, ID, Roll,marks,num,per):
        super().__init__(Name, Age, ID)
        self.Roll_no = Roll
        self.marks = list(marks)
        self.num = num
        self.per = per

    def Accept(self):
        super().Accept()
        try:
            self.Roll_no = int(input("Enter the Roll Number:"))
            self.num = int(input("Enter the How Many Subjects:"))

            if self.num <= 10:
                pass
            else:
                print("Enter the Valid Subject...")
            for i in range(self.num):
                M = int(input(f"Enter the Marks {i+1}:"))
                if 0 <= M <= 100:
                    self.marks.append(M)
                else:
                    print("Invalid Marks")
                    return
        except Exception as e:
            print("Exception is",e)

    def Calculate_Total(self):
        Total = sum(self.marks)
        print("Total marks Are:",Total)

    def Calculate_Per(self):
        self.per = sum(self.marks) / len(self.marks)
        print("Percetange is:",self.per)

    def Grade(self):
        if self.per >= 90:
            print("A ++")
        elif self.per<=89 and self.per >= 80:
            print("A")
        elif self.per<=79 and self.per >= 70:
            print("B+")
        elif self.per<=69 and self.per >= 60:
            print("B")
        elif self.per<=59 and self.per >= 50:
            print("C")
        elif self.per<=49 and self.per >= 35:
            print("Pass")
        else:
            print("Fail")

    def Display(self):

        super().Display()
        
        print("Roll Number :", self.Roll_no)
        print("Marks       :", self.marks)
        print("Total       :", self.Calculate_Total())
        print("Percentage  :", self.Calculate_Per())
        print("Grade       :", self.Grade())
    
class Teacher(Person):
    def __init__(self, Name, Age, ID,sub, Salary):
        super().__init__(Name, Age, ID)
        self.subject = sub
        self.__salary  = Salary

    def Accept(self):
        super().Accept()
        try:
            self.subject = input("Enter the Subject:")
            self.__salary = int(input("Enter the Salary"))
        except Exception as e:
            print("Exception is",e)

    def Increase_Salary(self):
        try:
            Add = int(input("Enter the Increase Salary:"))
            self.__salary += Add
            print(f"New Salary is {self.__salary} Subject Teacher {self.subject}")
        except Exception as e:
            print("Exception is:",e)
    def Display(self):
        super().Display()
        print("Salary",self.__salary)
        print("Subject:",self.subject)

    @staticmethod
    def Collegename():
        print("DES Pune")

    @classmethod
    def ShowTotal(cls):
        print("Total Persons are:",cls.Total_per)
def ShowInfo(obj):
    obj.Display()


teacher = Teacher("", 0, 0, "", 0)
student = Student("", 0, 0, 0, [], 0, 0)

while True:
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Display Student")
    print("4. Display Teacher")
    print("5. Total Persons")
    print("6. College Name")
    print("7. Exit")
    print("-"*40)

    try:
        choice = int(input("Enter the Choice:"))
        if choice == 1:
            student.Accept()
        elif choice == 2:
            teacher.Accept()
        elif choice == 3:
            student.Display()
        elif choice == 4:
            teacher.Display()
        elif choice == 5:
            teacher.ShowTotal()
        elif choice == 6:
            teacher.Collegename()
        elif choice == 7:
            print("Thank You...")
            break
        else:
            print("Enter the Choice Between 1 to 7")

    except Exception as e:
        print("Exception is:",e)

        
        








