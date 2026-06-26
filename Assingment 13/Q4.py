num=int(input("Enter the number:"))
binary=[]
while num>0:
    rem=num%2
    binary.append(rem)
    num=num // 2
for i in range(len(binary) - 1, -1, -1):
    print(binary[i], end="")
