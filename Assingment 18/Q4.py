# This is Q4.py in the 'Assingment 18' folder.
def main():
    no=int(input("Enter the Number:"))
    lst=[]
    for i in range(no):
        i=int(input("Enter the Number:"))
        lst.append(i)
    search=int(input("Enter the Number to Search:"))
    for i in lst:
        if i==search:
            print("Number is Fourd index is:",lst.index(i))
if __name__=="__main__":
    main()