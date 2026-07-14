# This is Q1.py in the 'Assingment 15' folder.
sq=lambda x:x*x
def main():
    num=int(input("Enter the how many Elements:"))
    lst=[]
    print("Enter the Elements:")
    for i in range(num):
        i=int(input())
        lst.append(i)
    ret=list(map(sq,lst))
    print(ret)


if __name__ == "__main__":
    main()