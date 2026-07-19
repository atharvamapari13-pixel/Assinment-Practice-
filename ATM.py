class ATM:
    def __init__(self):
        self.name = "Atharva"
        self.Ac_no = 541205741
        self.PIN = 131203
        self.balance = 5000
    def Deposit(self):
        try:
            Amount = int(input("Enter the Amount:")) 
            if Amount > 0:
                self.balance += Amount
                print("New Balance is:",self.balance)
        except Exception as e:
            print("Exception is:",e)
    def withdrow(self):
        try:
            new = int(input("Enter the 6 Digit PIN:"))
            if self.PIN == new:
                Amount = int(input("Enter the Amount:"))
                if Amount >= 0 and Amount <= self.balance:
                    self.balance = self.balance - Amount
                    print("New Balance is:",self.balance)
                else:
                    print("Balance is:",self.balance)
            else:
                print("Enter the Correct PIN")
        except Exception as e:
            print("Exception is:",e)
    def CheckBalance(self):
        try:
            new = int(input("Enter the 6 Digit PIN:"))
            if self.PIN == new:
                print("Balance is:",self.balance)
            else:
                print("Enter the Correct PIN")
        except Exception as e:
            print("Exception is:",e)
    def Changepin(self):
        try:
            new=int(input("Enter the PIN:"))
            if self.PIN == new:
                self.PIN = new
                print("PIN is Changed...")
            else:
                print("Incorrect PIN Enter the valid PIN")
        except Exception as e:
            print("Exception is:",e)
    def Display(self):
        try:
            new = int(input("Enter the 6 Digit PIN:"))
            if self.PIN == new:
                print("Name:",self.name)
                print("Account Number:",self.Ac_no)
                print("Balance:",self.balance)
            else:
                print("Enter the Correct PIN")
        except Exception as e:
            print("Exception is:",e)
obj = ATM()
while True:
    print("1. Deposit")
    print("2. withdrow")
    print("3. Check the Balance")
    print("4. Change PIN")
    print("5. Display")
    print("6. Exit..")
    try:
        num = int(input("Enter the Choice:"))
        if num == 1:
            obj.Deposit()
        elif num == 2:
            obj.withdrow()
        elif num == 3:
            obj.CheckBalance()
        elif num == 4:
            obj.Changepin()
        elif num == 5:
            obj.Display()
        elif num == 6:
            print("Thank You..")
            break
        else:
            print("Enter the Number Between range 1 to 6")
    except Exception as eobj:
        print("Exception is:",eobj)

            
    
        
