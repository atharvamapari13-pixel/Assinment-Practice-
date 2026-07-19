# This is Q3.py in the 'Assignment 28' folder.
import os
import time
def main():
    file = input("Enter the File name:")
    fobj = open(file,"r")
    for i in fobj:
        print(i)
        time.sleep(10)
if __name__ == '__main__':
    main()

