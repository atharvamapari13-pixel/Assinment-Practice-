# This is Q2.py in the 'Assingment 22' folder.
import multiprocessing
import time
import os
def factorial(num):
    fact=1
    for i in range(1, num+1):
        fact = fact * i
    return fact
def main():
    no=int(input("Enter the How many Elements:"))
    lst=[]
    Result=[]
    for i in range(no):
        i=int(input(f"Enter the Elements {i+1}:"))
        lst.append(i)
    
    start=time.perf_counter()
    pobj=multiprocessing.Pool()
    Result=pobj.map(factorial,lst)
    pobj.close()
    pobj.join()
    end=time.perf_counter()
    print("Process ID is:",os.getpid())
    print(Result)
    print(f"Total Required Time is {end - start:.4f} ")

if __name__ == "__main__":
    main()

