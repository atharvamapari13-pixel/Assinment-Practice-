# This is Q4.py in the 'Assingment 22' folder.
import os
import multiprocessing
import time
def Sum(No):
    print("Process ID :",os.getpid())
    sum=0
    for i in range(1, No+1):
        sum+= i ** 5
    return sum
def main():
    num=int(input("Enter the Number how many Elments:"))
    lst=[]
    result=[]
    for i in range(num):
        i=int(input(f"Enter the Number {i+1}:"))
        lst.append(i)
    
    pobj=multiprocessing.Pool()
    print("Process ID of main Process:",os.getpid())
    start=time.perf_counter()
    result=pobj.map(Sum,lst)
    end=time.perf_counter()
    print(result)
    print(f"Time is Required Is {end - start:.5f} seconds")
if __name__ == "__main__":
    main()
