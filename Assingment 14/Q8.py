A = lambda a,b : a+b
def main():
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    ret = A(n1,n2)
    print("Addition is:",ret)
if __name__=="__main__":
    main()