# This is Q7.py in the 'Assinment 16' folder.
def check(num):
    if num%5==0:
        return True
    else:
        return False
def main():
    no=int(input("Enter the Number:"))
    print(check(no))
if __name__=="__main__":
    main()
    