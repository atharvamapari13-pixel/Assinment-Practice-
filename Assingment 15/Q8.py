# This is Q8.py in the 'Assingment 15' folder.
new = lambda num : num if num % 5 == 0 and num % 3 == 0 else False
def main():
    num=int(input("Enter the Total Elements:"))
    Data=[]
    for i in range(num):
        i=int(input(f"Enter the Data {i+1}:"))
        Data.append(i)
    ret=list (filter(new,Data))
    print(ret)
if __name__=="__main__":
    main()