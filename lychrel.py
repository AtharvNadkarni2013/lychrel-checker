import datetime

def reverseNumber(number):
    rnum = 0
    while number > 0:
        rem = number % 10
        rnum = rnum * 10 + rem
        number = number // 10
    return rnum

rev = reverseNumber

def checkPalindrome(number):
    rnum = rev(number)
    return number == rnum

cp = checkPalindrome

def reverseAdd(number):
    return number + rev(number)

ra = reverseAdd

def checkLychrel(number, iter=5000000):
    for i in range(iter):
        ranum = ra(number)
        if cp(ranum):
            return False
    return True

cl = checkLychrel


number = int(input("Enter a number: "))
print(f"Checking if {number} is Lychrel, over 5,000,000 iterations!")
before_exec = datetime.datetime.now()
if cl(number):
    print(f"{number} is Lychrel")
else:
    print(f"{number} is not Lychrel")