# This is Q4.py in the 'Assignment 30' folder.
import schedule
import time
def Display():
    print("Namskar...")
def main():
    print("Automation is Started...")
    schedule.every().day.at("09:30").do(Display)
    while True:
        schedule.run_pending()
        time.sleep(50)
    
if __name__ == "__main__":
    main()