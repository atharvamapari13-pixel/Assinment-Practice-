# This is Q1.py in the 'Assingment 21' folder.
import threading
def check_prime(lst):
    for num in lst:
        if num < 2:
            continue
        isPrime=True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                isPrime = False
                break

        if isPrime:
            print(num, end=" ")
    print()
def check_not_prime(lst):
    print("Non-Prime Numbers:")
    for num in lst:
        if num < 2:
            print(num, end=" ")
            continue

        isPrime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                isPrime = False
                break

        if not isPrime:
            print(num, end=" ")
    print()
    
def main():
    no=int(input("Enter the How many Elements:"))
    lst=[]
    for i in range(no):
        i=int(input(f"Enter the Elements {i+1}:"))
        lst.append(i)
    t1=threading.Thread(target=check_prime,args=(lst,))
    t2=threading.Thread(target=check_not_prime,args=(lst,))
    t1.start()
    t2.start()


    
if __name__=="__main__":
    main()
