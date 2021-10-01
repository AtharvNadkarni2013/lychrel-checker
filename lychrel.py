import datetime

def reverseNumber(num):
    rnum = 0
    while num > 0:
        rem = num % 10
        rnum = rnum * 10 + rem
        num = num // 10
    return rnum

rev = reverseNumber

def checkPalindrome(num):
    rnum = rev(num)
    return num == rnum

cp = checkPalindrome

def reverseAdd(num):
    return num + rev(num)

ra = reverseAdd

def checkLychrel(num, iter=5000000):
    for i in range(iter):
        ranum = ra(num)
        if cp(ranum):
            return False
    return True

cl = checkLychrel


num = int(input("Enter a num: "))
print(f"Checking if {num} is Lychrel, over 5,000,000 iterations!")
before_exec = datetime.datetime.now()
if cl(num):
    print(f"{num} is Lychrel")
else:
    print(f"{num} is not Lychrel")