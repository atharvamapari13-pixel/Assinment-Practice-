# This is Q3.py in the 'Assignment 31' folder.
import os 
import datetime
import schedule
import time
def scan(Floder = r"E:\Marvellous Assinment"):
    print("Files from the Directory")
    fobj = open("Log1.txt",'a')
    if not os.path.exists(Floder):
        print("Directory does not exist.")
        return
    scount = 0
    Fcount = 0
    for Flodername, Subfloder, Filename in os.walk(Floder):
        for Sub in Subfloder:
            scount += 1
        for Fname in Filename:
            Fcount += 1
    fobj.write(f"Total Sub Floder are There: {scount}\n")
    fobj.write(f"Total Files Are There: {Fcount}\n")
    fobj.write(f"Scan Time: {datetime.datetime.now()}\n")
    fobj.write("-" * 40 + "\n")
def main():
    print("Script is Started...")
    schedule.every(2).seconds.do(scan)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()

