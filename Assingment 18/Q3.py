# This is Q3.py in the 'Assingment 18' folder.
def main():
    no=int(input("Enter the Number:"))
    lst=[]
    for i in range(no):
        i=int(input("Enter the Number:"))
        lst.append(i)
    print("the maximum number is:",min(lst))
if __name__=="__main__":
    main()