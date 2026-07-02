# This is Q4.py in the 'Assingment 15' folder.
from functools import reduce
add = lambda a,b:a+b
def main():
    num=int(input("Enter the Total Elements:"))
    Data=[]
    for i in range(num):
        i=int(input(f"Enter the Data {i+1}:"))
        Data.append(i)
    ret = reduce(add, Data)
    print(ret)
if __name__=="__main__":
    main()

