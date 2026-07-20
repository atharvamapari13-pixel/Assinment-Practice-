# This is Q1.py in the 'Assignment 28' folder.
import os

def main():
    file = input("Which file Do u want to perform operations:")
    fobj = open(file,"w")
    print("File has been Opened...")
    fobj.write("Hello This is Practice Set...")
    fobj.close()
    pobj = open("Demo.txt",'r')
    count = 0
    for i in pobj:
        count = count + 1
    print("Total number of Lines:",count)
    pobj.close()
    

if __name__ == "__main__":
    main()