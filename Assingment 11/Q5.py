num=int(input("Enter the Number:"))
rev=0
original = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if (original == rev):
    print("Number is Palindrome...")
else:
    print("Number is not Palindrome")
