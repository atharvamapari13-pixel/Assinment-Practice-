# This is Q2.py in the 'Assingment 15' folder.
even = lambda x : x%2 == 0
def main():
    num=int(input("Enter the Number of Elements:"))
    Data=[]
    for i in range(num):
        i=int(input("Enter the Data:"))
        Data.append(i)
    ret=list(filter(even, Data))
    print(ret)
if __name__ == "__main__":
    main()

