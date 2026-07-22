# This is Q3.py in the 'Assingment 29' folder.
import sys
import os
import shutil
def Check(Filename):
    Destination = "New Floder"
    fobj = open(Filename,'r')
    if not os.path.exists(Filename):
        print("File is not There")
        return
    if not os.path.exists(Destination):
        print("Path Is not Destination")
        return
    shutil.copy(Filename,Destination)
    print("File Copied Successfully...")
    
def main():
    if len(sys.argv) == 2:
        Check(sys.argv[1])
    else:
        print("Enter the Command Line Argument.<filename>")
    
         
if __name__ == "__main__":
    main()