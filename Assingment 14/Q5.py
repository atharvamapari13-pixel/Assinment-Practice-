ex = lambda num : num if num%2==0 else False
def main():
    n=int(input("Enter a number:"))
    ret = ex(n)
    if ret==False:
        print("Number is odd")
    else:
        print("Number is even")
if __name__=="__main__":
    main()