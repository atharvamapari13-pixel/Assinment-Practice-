# This is Q4.py in the 'Assingment 21' folder.
import threading
def sumof(lst):
    sum=0
    for i in lst:
        sum+=i
    print(sum)
def product(lst):
    prod=1
    for i in lst:
        prod *= i
    print(prod)
    
def main():
    num=int(input("Enter the How many Elements:"))
    lst=[]
    for i in range(num):
        i=int(input("Enter the Number:"))
        lst.append(i)
    t1=threading.Thread(target=sumof,args=(lst,))
    t2=threading.Thread(target=product,args=(lst,))
    t1.start()
    t2.start()
if __name__=="__main__":
    main()
