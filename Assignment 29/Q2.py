# This is Q2.py in the 'Assingment 29' folder.
def main():
    File=input("Enter the File name:")
    fobj = open(File,'r')
    for i in fobj:
        print(i)
if __name__=='__main__':
    main()