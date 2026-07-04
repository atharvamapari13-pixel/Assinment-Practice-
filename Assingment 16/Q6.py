# This is Q6.py in the 'Assinment 16' folder.
def check(num):
    if num==0:
        print("Zero")
    elif num>0:
        print("Positive")
    else:
        print("Negative")
def main():
    no=int(input("Enter the Number:"))
    check(no)
if __name__=="__main__":
    main()