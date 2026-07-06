# This is Q5.py in the 'Assingment 20' folder.
import threading
def inorder(no):
    for i in range(1,no+1):
        print(i)
def reverse(no):
    for i in range(no,1-1,-1):
        print(i)
def main():
    num=int(input("Enter the Number:"))
    t1=threading.Thread(target=inorder, args=(num,))
    t2=threading.Thread(target=reverse, args=(num,))
    t1.start()
    t2.start()
if __name__ == "__main__":
    main()
