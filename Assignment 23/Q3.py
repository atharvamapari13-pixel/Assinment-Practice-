# This is Q3.py in the 'Assingment 23' folder.
import multiprocessing
import time
import os
def Sum_count(no):
    count=0
    #print("Process ID:",os.getppid())
    for i in range(2,no+1,2):
        count+=1
    return count
def main():
    no=int(input("Enter the How many Elements whants:"))
    lst=[]
    result=[]
    for i in range(no):
        i=int(input(f"Enter the Elements {i+1}:"))
        lst.append(i)
    cores=multiprocessing.cpu_count()
    print(cores)
    pobj=multiprocessing.Pool(processes=cores)
    print("Process ID:",os.getppid())
    start_time=time.perf_counter()
    result=pobj.map(Sum_count,lst)
    pobj.close()
    pobj.join()
    end_time=time.perf_counter()
    print(result)
    print(f"Total Required Timing is {end_time - start_time} seconds ")
if __name__=="__main__":
    main()