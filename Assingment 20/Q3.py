# This is Q3.py in the 'Assingment 20' folder.
import threading
def Even_lst(lst):
    even_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
    print(even_sum)
    
def Odd_lst(lst):
    odd_sum = 0
    for i in lst:
        if i % 2 != 0:
            odd_sum += i
    print(odd_sum)

def Accept(Num):
    lst = []
    for i in range(Num):
        lst.append(int(input(f"Enter a number {i+1}: ")))
    return lst
def main():
    num = int(input("Enter a number: "))
    lst = Accept(num)
    obj2 = threading.Thread(target=Odd_lst, args=(lst,))
    obj3 = threading.Thread(target=Even_lst, args=(lst,))
    obj2.start()
    obj3.start()
    obj2.join()
    obj3.join()
    print("Exit from main")
    print("Thread ID: ",threading.get_ident())
if __name__ == "__main__":
    main()


