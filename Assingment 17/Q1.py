# This is Q1.py in the 'Assinment 17' folder.
from Arithmatic import *
def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition:", Add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", Multiply(a, b))
    print("Division:", divide(a, b))
if __name__ == "__main__":
    main()