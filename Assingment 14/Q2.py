cube=lambda num:num*num*num
def main():
    n=int(input("Enter a number:"))
    ret = cube(n)
    print("Cube is:",ret)
if __name__=="__main__":
    main()