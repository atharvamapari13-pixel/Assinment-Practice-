# This is Q8.py in the 'Assinment 16' folder.
def pattern(no):
    for i in range(no):
        print("*", end=" ")
def main():
    no=int(input("Enter the Number:"))
    pattern(no)
if __name__=="__main__":
    main()