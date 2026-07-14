new = lambda a,b,c : a if a>b and a>c else b if b>c else c
def main():
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    n3=int(input("Enter third number:"))
    ret = new(n1,n2,n3)
    print("Maximum is:",ret)
if __name__=="__main__":
    main()