# This is Q5.py in the 'Assignment 28' folder.
import os
def main():
    file = input("Enter the file name:")
    fobj = open(file,'r')
    word = input("Enter the Word to find:")
    count = 0
    for i in fobj:
        new=i.split()
        if word in new:
            count += 1
            continue
    if count>0:
        print("Word is Present in file Total Occurance is:",count)
    else:
        print("There is no word")
    fobj.close()
if __name__ == '__main__':
    main()