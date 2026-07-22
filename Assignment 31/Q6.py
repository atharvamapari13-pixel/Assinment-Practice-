# This is Q6.py in the 'Assignment 31' folder.
import schedule
def weekly_goal():
    print("Monday at 09:00 AM = Starts your weekly Goal")
def progress():
    print("wednesdat at 05:00 PM = Review your weekly progress")
def Complete():
    print("Friday at 06:00 PM = weekly work completed")
def main():
    schedule.every().monday.at("09:00").do(weekly_goal)
    schedule.every().wednesday.at("17:00").do(progress)
    schedule.every().friday.at("18:00").do(Complete)
    while True:
        schedule.run_pending()
if __name__ == "__main__":
    main()