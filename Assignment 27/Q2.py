# This is Q2.py in the 'Assignment 27' folder.
class Bank_Accout:
    ROI = 10.5
    def __init__(self, Name, Accout):
        self.name = Name
        self.Account_Number = Accout
        self.Balance = 1500
    def Deposit(self):
        Amount=int(input("Enter the Amount:"))
        self.Balance += Amount
        print("New Balance:",self.Balance)
    def withdrow(self):
        try:
            Amount=int(input("Enter the Amount:"))
            if (self.Balance >= Amount):
                self.Balance -= Amount
                print("New Balance:",self.Balance)
            else:
                print(f"Your Account Currently Having Amount is {self.Balance}")
        except Exception as n:
            print("Exception is here",n)
    @classmethod
    def CalculateInterest(cls):
        Amount=int(input("Enter the Amount:"))
        Interest = (Amount * cls) / 100
        print("Total Interest Should u get is:",Interest)
    def Display(self):
        print("Name:",self.name)
        print("Account Number:",self.Account_Number)
        print("Balance:",self.Balance)
    
obj=Bank_Accout("Atharva",123456)
while True:

    print("1. Deposit")
    print("2. withdraw")
    print("3. Display")
    print("4. Interest")
    print("5. Exit")
    print('--'*40)
    try :
        num = int(input("Enter the Option Any one:"))
        if num == 1:
            obj.Deposit()
        elif num == 2:
            obj.withdrow()
        elif num == 3:
            obj.Display()
        elif num == 4:
            obj.CalculateInterest()
        elif num == 5:
            print("Thank u...")
            break
        else:
            print("Enter the Number Between 1 to 5")
    except Exception as abc:
        print("Exception is:",abc)

    

    

