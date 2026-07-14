def fact(num):
    if (num<=1):
        return 1
    else:
        return num * fact(num - 1)
a=int(input("Enter The Number:"))
res=fact(a)
print(res)