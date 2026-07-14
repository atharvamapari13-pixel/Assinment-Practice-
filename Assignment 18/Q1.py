# This is Q1.py in the 'Assingment 18' folder.
def Add(Num):
    sum=0
    for i in Num:
        sum=sum+i
    return sum
def main():
    num=int(input("Enter the Number:"))
    lst=[]
    for i in range(num):
       i=int(input("Enter the Number:"))
       lst.append(i)
    ret=Add(lst)
    print("The Sum of the List is:",ret)
if __name__=="__main__":
    main()