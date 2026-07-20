# This is Q5.py in the 'Assingment 29' folder.
import sys
import os
def Occurance(Fname, word):
    fobj = open(Fname, 'r')
    count = 0
    for i in fobj:
        words = i.split()
        if word in words:
            count += words.count(word)
    fobj.close()
    return count
def main():
    if len(sys.argv) == 3:
        Ret = Occurance(sys.argv[1],sys.argv[2]) 
        print(Ret)
    else:
        print("Check the Command Line Arguments...")
if __name__ == "__main__":
    main()