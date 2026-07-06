# This is Q3.py in the 'Assingment 21' folder.
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for i in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

def main():
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    t3 = threading.Thread(target=increment)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final Counter Value:", counter)

if __name__ == "__main__":
    main()