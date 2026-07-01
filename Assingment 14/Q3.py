maximum = lambda a,b: a if a>b else b
def main():
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    ret = maximum(n1,n2)
    print("Maximum is:",ret)
if __name__=="__main__":
    main()