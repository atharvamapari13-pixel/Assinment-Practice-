# This is Q2.py in the 'Assingment 20' folder.
import threading

def fact_even(Num):
    even_sum = 0
    print("Even factors are:", end=" ")
    for i in range(1, Num + 1):
        if Num % i == 0 and i % 2 == 0:
            print(i, end=" ")
            even_sum += i
    print("\nSum of even factors is:", even_sum)


def fact_odd(Num):
    odd_sum = 0
    print("Odd factors are:", end=" ")
    for i in range(1, Num + 1):
        if Num % i == 0 and i % 2 != 0:
            print(i, end=" ")
            odd_sum += i
    print("\nSum of odd factors is:", odd_sum)


def main():
    Num = int(input("Enter a number: "))

    t1 = threading.Thread(target=fact_even, args=(Num,))
    t2 = threading.Thread(target=fact_odd, args=(Num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()