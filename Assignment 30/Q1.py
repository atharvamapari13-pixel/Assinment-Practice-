# This is Q1.py in the 'Assignment 30' folder.
import schedule
import time
def Display():
    print("Jay Ganesh....")
def main():
    print("Automation is Started...")
    schedule.every(2).seconds.do(Display)
    while True:
        schedule.run_pending()


if __name__=="__main__":
    main()