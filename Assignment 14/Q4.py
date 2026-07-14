minimum = lambda a,b: a if a<b else b
def main():
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    ret = minimum(n1,n2)
    print("Minimum is:",ret)
if __name__=="__main__":
    main()