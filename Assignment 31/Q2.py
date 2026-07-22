# This is Q2.py in the 'Assignment 31' folder.
# This is Q1.py in the 'Assignment 31' folder.
import schedule
import time
def display(msg):
    print(msg)
def main():
    msg = input("Enter a Message:")
    second = int(input("Enter how many seconds:"))
    if (second >= 1):
        schedule.every(second).seconds.do(display, msg)
    else:
        print("Enter the valid seconds...")
    while True:
        schedule.run_pending()
if __name__=="__main__":
    main()