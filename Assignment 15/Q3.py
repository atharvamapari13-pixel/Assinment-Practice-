# This is Q3.py in the 'Assingment 15' folder.
odd = lambda X : X % 2 != 0
def main():
    num=int(input("Enter the Total Elements:"))
    Data=[]
    for i in range(num):
        i=int(input(f"Enter the Data {i+1}:"))
        Data.append(i)
    ret=list(filter(odd,Data))
    print(ret)
if __name__=="__main__":
    main()