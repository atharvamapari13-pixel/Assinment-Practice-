# This is Q10.py in the 'Assingment 15' folder.
from functools import reduce
maximum = lambda num : num % 2 == 0
def main():
    num=int(input("Enter the Total Elements:"))
    Data=[]
    for i in range(num):
        i=int(input(f"Enter the Data {i+1}:"))
        Data.append(i)
    ret=list(filter(maximum,Data))
    print(len(ret))
if __name__=="__main__":
    main()