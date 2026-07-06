# This is Q4.py in the 'Assingment 20' folder.
import threading
def lowercheck(string):
    lower=[]
    for i in string:
        if i.islower():
            lower.append(i)
    print("Lowercase letters:", lower)
    print("Lower Thread ID:", threading.get_ident())
def Uppercheck(string):
    upper = []
    for i in string:
        if i.isupper():
            upper.append(i)
    print("Upper letters:", upper)
    print("Upper Thread ID:", threading.get_ident())
def Digitcheck(string):
    digit=[]
    for i in string:
        if i.isdigit():
            digit.append(i)
    print("Digits :", digit)
    print("digit Thread ID:", threading.get_ident())
def main():
    string = input("Enter a string: ")
    small_thread = threading.Thread(target=lowercheck, args=(string,))
    capital_thread = threading.Thread(target=Uppercheck, args=(string,))
    digit_thread = threading.Thread(target=Digitcheck, args=(string,))
    print("Thread ID: ", threading.get_ident())
    small_thread.start()
    capital_thread.start()
    digit_thread.start()
   # small_thread.join()
   # capital_thread.join()
   # digit_thread.join()
    
if __name__ == "__main__":
    main()