# This is Q5.py in the 'Assingment 18' folder.
def check_prime(lst):
    sum=0
    for i in lst:
        if i<2:
            continue
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            sum+=i
    return sum   
def main():
    no=int(input("Enter the Number:"))
    lst=[]
    for i in range(no):
        i=int(input("Enter the Number:"))
        lst.append(i)
    print("the sum of prime numbers is:",check_prime(lst))
if __name__=="__main__":
    main()