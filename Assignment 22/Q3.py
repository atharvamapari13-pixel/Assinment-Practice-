# This is Q3.py in the 'Assingment 22' folder.
import multiprocessing
import time
import os
def isPrime(num):
    if num<2:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    return True
def Count_Prime(N):
    count=0
    for i in range(1,N+1):
        if isPrime(i):
            count+=1
    return count
def main():
    no=int(input("Enter the how many Elements:"))
    lst=[]
    result=[]
    for i in range(no):
        i=int(input(f"Enter the Number {i+1}:"))
        lst.append(i)
    start=time.perf_counter()
    pobj=multiprocessing.Pool()
    result=pobj.map(Count_Prime,lst)
    pobj.close()
    pobj.join()
    end=time.perf_counter()
    print(result)
    print(f"Total Time Required is {end - start}")
if __name__ == "__main__":
    main()

