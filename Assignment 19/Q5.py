# This is Q5.py in the 'Assingment 19' folder.
from functools import reduce

def check_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
multi = lambda num:num*2
maximum = lambda num1,num2:num1 if num1>num2 else num2
def main():
    no=int(input("Enter the Number:"))
    lst=[]  
    for i in range(no):
        i=int(input(f"Enter the Number {i+1}:"))
        lst.append(i)
    #fun=check_prime(lst)
    ret1=list(filter(check_prime,lst))
    ret2=list(map(multi,ret1))
    #ret3=reduce(maximum,ret2)
    if ret2:
        ret3=reduce(maximum,ret2)
        print("The Filtered List is:",ret1)
        print("The Mapped List is:",ret2)
        print("The Maximum Value is:",ret3)
    else:
        print("No prime numbers found in the list.")
if __name__ == "__main__":
    main()

