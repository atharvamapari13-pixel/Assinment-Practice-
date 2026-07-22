# This is Q4.py in the 'Assignment 31' folder.
import schedule
import datetime
import time
def Create_log():
    timestamp = datetime.datetime.now()
    Logfile = "Marvellous %s.log"%(timestamp)
    Logfile=Logfile.replace(" ","_")
    Logfile=Logfile.replace(":","_")
    print("Log File has been Created:",Logfile)
    fobj = open(Logfile,'w')
    fobj.write("Log File has Created Successfully\n")
    fobj.write(f"Current Time: {datetime.datetime.now()}")

def main():
    Create_log()
    schedule.every(10).minutes.do(Create_log)
    while True:
        schedule.run_pending()
        time.sleep(50)
if __name__ == "__main__":
    main()