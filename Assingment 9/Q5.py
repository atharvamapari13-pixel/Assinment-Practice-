def div(a):
    if a % 3 == 0 and a % 5 == 0:
        print("Number is Divisible by 3 and 5")
    else:
        print("Number is not Divisible by 3 and 5")
A=int(input("Enter the Number:"))
res=div(A)
print(res)
