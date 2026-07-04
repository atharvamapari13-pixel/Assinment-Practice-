# This is Q2.py in the 'Assinment 16' folder.
def chkeven(Num):
    if Num%2==0:
        print(f"{Num} is Even Number")
    else:
        print(f"{Num} is Odd Number")
def main():
    Num=int(input("Enter the Number:"))
    chkeven(Num)    
if __name__=="__main__":
    main()