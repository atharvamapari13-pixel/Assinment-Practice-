# This is Q2.py in the 'Assingment 23' folder.
import multiprocessing
import os
import time
def Sum_odd(no):
    sum=0
    print("Process ID:",os.getppid())
    for i in range(1,no+1,2):
        sum+=i
    return sum
def main():
    no=int(input("Enter the How many Elements whants:"))
    lst=[]
    result=[]
    for i in range(no):
        i=int(input(f"Enter the Elements {i+1}:"))
        lst.append(i)
    obj=multiprocessing.Pool()
    print("Process ID:",os.getppid())
    start_time=time.perf_counter()
    result=obj.map(Sum_odd,lst)
    obj.close()
    obj.join()
    end_time=time.perf_counter()
    print(result)
    print(f"Total Required Timing is {end_time - start_time} seconds ")
if __name__ == "__main__":
    main()