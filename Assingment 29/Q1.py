# This is Q1.py in the 'Assingment 29' folder.
import os
import sys

def Check(DicName , name):
    Ret = False
    Ret = os.path.exists(DicName)
    if (Ret == False):
        print("Marvellous Automation Error : There is No Such Directory with name",DicName)
        return
    Ret = os.path.isdir(DicName)
    if (Ret == False):
        print("Marvellous Automation Error : It is not a Directory with name",DicName)
        return
    for Foldername, Subfolder, Fname in os.walk(DicName):
        for Filename in Fname:
            if Filename == name:
                return True
    print("file is not there...")
    return False
def main():
    Folder=input("Enter the Folder Name:")
    File=input("Enter the File name:")
    Ret = Check(Folder,File)
    print("Result",Ret)
if __name__=="__main__":
    main()