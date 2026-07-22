# This is Q5.py in the 'Assignment 30' folder.
import schedule
import datetime
import time
def Create_write():
    fobj = open("new1.txt",'a')
    fobj.write(f"Tack Executed : {datetime.datetime.now()}")
    fobj.close()
def main():
    schedule.every(3).seconds.do(Create_write)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()