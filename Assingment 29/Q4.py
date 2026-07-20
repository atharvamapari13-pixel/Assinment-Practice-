# This is Q4.py in the 'Assingment 29' folder.
import hashlib
import sys
def CheckSum(Fname1, Fname2):
    fobj = open(Fname1,'rb')
    fobj1 = open(Fname2, 'rb')
    hobj = hashlib.md5()
    hobj1 = hashlib.md5()

    Buffer = fobj.read(1000)
    Buffer1 = fobj1.read(1000)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)
    while(len(Buffer1)>0):
        hobj1.update(Buffer1)
        Buffer1 = fobj1.read(1000)
    fobj.close()
    fobj1.close()
    if hobj.hexdigest() == hobj1.hexdigest():
        print("Both Files Are same")
    else:
        print("Both File Are Different...")


def main():
    if len(sys.argv)==3:
        CheckSum(sys.argv[1], sys.argv[2])
    else:
        print("Command Line Error Occured...")
if __name__ =="__main__":
    main()