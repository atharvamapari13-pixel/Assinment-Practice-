
num=int(input("Enter the Number:"))
sum=0
for i in range(1,num):
    if num % i == 0:
        sum+=i
if(num == sum):
    print("Number is perfect")
else:
    print("Number is not perfect")
