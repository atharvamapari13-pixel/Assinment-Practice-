Div = lambda num : num if num%5==0 else False
def main():
    n=int(input("Enter a number:"))
    ret = Div(n)
    if ret==False:
        print("Number is not divisible by 5")
    else:
        print("Number is divisible by 5")
if __name__=="__main__":
    main()
