def prime(num):
    if num<= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
a=int(input("Enter the number:"))
res=prime(a)
if res == True:
    print("Number is Prime")
else:
    print("Number is not prime")