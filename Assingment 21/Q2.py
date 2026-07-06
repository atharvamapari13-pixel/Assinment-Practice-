# This is Q2.py in the 'Assingment 21' folder.
import threading
def maximum(lst):
    print(max(lst))
def minimum(lst):
    print(min(lst))
def main():
    num=int(input("Enter the How many Elements:"))
    lst=[]
    for i in range(num):
        i=int(input(f"Enter the Number {i+1}:"))
        lst.append(i)
    t1=threading.Thread(target=maximum,args=(lst,))
    t2=threading.Thread(target=minimum,args=(lst,))
    t1.start()
    t2.start()
if __name__=="__main__":
    main()
