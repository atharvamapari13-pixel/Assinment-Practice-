# This is Q3.py in the 'Assinment 17' folder.
def fact(num):
    if num<0 and num == 1:
        print(1)
    else:
        fact = 1
        for i in range(1,num+1):
            fact = fact*i
        print(fact)
def main():
    num=int(input("Enter a number:"))
    fact(num)
if __name__=="__main__":
    main()