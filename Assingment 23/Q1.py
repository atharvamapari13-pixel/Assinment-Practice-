# This is Q1.py in the 'Assingment 23' folder.
import multiprocessing
import os
import time
def Sum_even(Num):
    print("Process ID:",os.getppid())
    sum=0
    for i in range(2,Num+1,2):
        sum+=i
    return sum
def main():
    num=int(input("Enter the How many Elements:"))
    lst=[]
    result=[]
    for i in range(num):
        i=int(input(f"Enter the Elements {i+1}:"))
        lst.append(i)
    pobj=multiprocessing.Pool()
    print("Process ID:",os.getppid())
    start=time.perf_counter()
    result=pobj.map(Sum_even,lst)
    pobj.close()
    pobj.join()
    end=time.perf_counter()
    print(result)
    print(f"Time Required is {end - start:.4f} seconds")
if __name__ == "__main__":
    main()

