# This is Q1.py in the 'Assingment 22' folder.
import multiprocessing
def Square(num):
    return num * num
def main():
    no=int(input("Enter the How many Elements:"))
    lst=[]
    Result=[]
    for i in range(no):
        i=int(input(f"Enter the Elements {i+1}:"))
        lst.append(i)
    pobj=multiprocessing.Pool()
    Result = pobj.map(Square,lst)
    pobj.close()
    pobj.join()
    print("Result is:")
    print(Result)
if __name__=="__main__":
    main()