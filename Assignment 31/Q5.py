# This is Q5.py in the 'Assignment 31' folder.
import os 
import datetime
import schedule
import time
def scan(Floder = r"E:\Marvellous Assinment"):
    print("Files from the Directory")
    fobj = open("DirectoryCount.txt",'a')
    if not os.path.exists(Floder):
        print("Directory does not exist.")
        return
    Fcount = 0
    for Flodername, Subfloder, Filename in os.walk(Floder):
        for Fname in Filename:
            Fcount += 1
    fobj.write(f"Directory Path: {Floder}\n")
    fobj.write(f"Total Files Are There: {Fcount}\n")
    fobj.write(f"Scan Time: {datetime.datetime.now()}\n")
    fobj.write("-" * 40 + "\n")
def main():
    scan()
    #schedule.every(5).minutes.do(scan)
    #while True:
        #schedule.run_pending()
        #time.sleep(50)
if __name__ == "__main__":
    main()