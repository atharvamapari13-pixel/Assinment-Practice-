# This is Q7.py in the 'Assingment 15' folder.
Greater = lambda str : len(str)>= 5
def main():
    num=int(input("Enter the Total Elements:"))
    Data=[]
    for i in range(num):
        i=input(f"Enter the Data (String) {i+1}:")
        Data.append(i)
    ret=list(filter(Greater,Data))
    print(ret)
if __name__=="__main__":
    main()