# This is Q4.py in the 'Assingment 23' folder.
import multiprocessing
import time
import os
def odd_count(no):
    count=0
    print("Process ID:",os.getppid())
    for i in range(no+1):
        if i % 2 != 0:
            count+=1
    return count
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
    result=obj.map(odd_count,lst)
    end_time=time.perf_counter()
    obj.close()
    obj.join()
    print(result)
    print(f"Total Required Timing is {end_time - start_time} seconds ")
if __name__=="__main__":
    main()