# This is Q3.py in the 'Assingment 19' folder.
from functools import reduce
condition = lambda num : num>=70 and num<=90
Add = lambda num:num+10
product = lambda num1,num2:num1*num2
def main():
    no=int(input("Enter the Number:"))
    lst=[]
    for i in range(no):
        i=int(input("Enter the Number:"))
        lst.append(i)
    ret1=list(filter(condition,lst))
    ret2=list(map(Add,ret1))
    ret3=reduce(product,ret2)
    print("The Filtered List is:",ret1)
    print("The Mapped List is:",ret2)
    print("The Reduced Value is:",ret3)
if __name__=="__main__":
    main()


    