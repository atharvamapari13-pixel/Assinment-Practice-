# This is Q2.py in the 'Assignment 30' folder.
import schedule
import datetime
import time
def Display():
    print("Current Date time is:",datetime.datetime.now())
def main():
    schedule.every(1).minutes.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(50)
    
if __name__ == "__main__":
    main()