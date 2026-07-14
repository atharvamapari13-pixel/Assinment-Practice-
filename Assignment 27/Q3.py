# This is Q3.py in the 'Assignment 27' folder.
class Numbers:

    def __init__(self):
        self.value = 0

    def check_prime(self):

        try:
            self.value = int(input("Enter the Number:"))
            
            if self.value<=2:
                print("Number is Not Prime..")
            else:
                isPrime=True
                for i in range(2,int(self.value**0.5) + 1):
                    if self.value % i == 0:
                        isPrime = False
                        break
                if isPrime:
                    print("Number is Prime")
                else:
                    print("Number is Not Prime")

        except Exception as e:
            print("Exception is:",e)

        
    def chkperfect(self):

        try:
            self.value = int(input("Enter the Number:"))
            Sum = 0
            for i in range(1, self.value):
                if self.value % i == 0 :
                    Sum += i
            if Sum == self.value:
                print("Number is Perfect...")
            else:
                print("Number is Not Perfect....")

        except Exception as e:
            print("Exception is:",e)
        
    def Factors(self):

        try:
            self.value = int(input("Enter the Number:"))
            fact=1
            for i in range(1,self.value):
                fact +=  fact * i
            print("Factorial is:",fact)

        except Exception as e:
            print("Exception is:",e)
      
    def Sum_Factors(self):

        try:
            self.value = int(input("Enter the Number:"))
            fact=1
            lst=[]
            new=[]
            for i in range(1, self.value):
                lst.append(i)
            for i in (lst):
                fact +=  fact * i
                new.append(fact)
            new1=1+sum(new)
            print("Sum of the Factorial is:",new1)   

        except Exception as e:
            print("Exception is:",e)
        
obj=Numbers()

while True:
    print("1. Check Prime")
    print("2. Check Perfect")
    print("3. Factorial of Number:")
    print("4. Sum of Factorial Till The Number u Entered...")
    print("5. Exit...")
    print("--"*40)

    try:
        num=int(input("Enter the Choice:"))
        if num == 1:
            obj.check_prime()
        elif num == 2:
            obj.chkperfect()
        elif num == 3:
            obj.Factors()
        elif num == 4:
            obj.Sum_Factors()
        elif num == 5:
            print("Thank You...")
            break
        else:
            print("Enter the Valid Choice...")

    except Exception as e:
        print("Exception is:",e)

        