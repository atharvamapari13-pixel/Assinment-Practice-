# This is Q4.py in the 'Assingment 19' folder.
from functools import reduce
Even=lambda num:num%2==0
sq=lambda num:num*num
Add = lambda num1,num2:num1+num2
def main():
    no=int(input("Enter the Number:"))
    lst=[]
    for i in range(no):
        i=int(input(f"Enter the Number {i+1}:"))
        lst.append(i)
    ret1=list(filter(Even,lst))
    ret2=list(map(sq,ret1))
    ret3=reduce(Add,ret2)
    print("Even Number in the List:",ret1)
    print("Square of the Even number is:",ret2)
    print("Addition of the Even Number is:",ret3)
if __name__=="__main__":
    main()