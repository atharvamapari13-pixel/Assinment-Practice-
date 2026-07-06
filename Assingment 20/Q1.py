# This is Q1.py in the 'Assingment 20' folder.
import threading
def createEven():
    for i in range(2, 21, 2):
        print(i)
    print("Even numbers printed")
def createOdd():
    for i in range(1, 20, 2):
        print(i)
    print("Odd numbers printed")
def main():
    t1=threading.Thread(target=createEven)
    t2=threading.Thread(target=createOdd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()