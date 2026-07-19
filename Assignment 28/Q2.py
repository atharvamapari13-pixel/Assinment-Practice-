# This is Q2.py in the 'Assignment 28' folder.
import os
def main():
    file = input("Enter the File name:")
    fobj = open (file,"r")
    count = 0
    for i in fobj:
        new=i.split()
        count = count + len(new)
    print(new)
    print("Total numbers of words:",count)
if __name__ == "__main__":
    main()
