# This is Q6.py in the 'Assignment 30' folder.
import schedule

def Lunch():
    print("Lunch time at 01:00 PM")
def wrap():
    print("wrap up at 06:00 PM")
def main():
    schedule.every("01:00").days.do(Lunch)
    schedule.every("06:00").days.do(wrap)
    while True:
        schedule.run_pending()
if __name__=="__main__":
    main()


