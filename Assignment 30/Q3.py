# This is Q3.py in the 'Assignment 30' folder.
import schedule
import time
def Display():
    print("Coding Kar !...")
def main():
    schedule.every(30).minutes.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(50)
    
if __name__ == "__main__":
    main()