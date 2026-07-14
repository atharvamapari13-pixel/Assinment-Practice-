# This is Q6.py in the 'Assingment 15' folder.
from functools import reduce
minimum = lambda a,b: a if a<b  else b
def main():
    num=int(input("Enter the Total Elements:"))
    Data=[]
    for i in range(num):
        i=int(input(f"Enter the Data {i+1}:"))
        Data.append(i)
    ret=reduce(minimum,Data)
    print(ret)
if __name__=="__main__":
    main()