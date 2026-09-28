# 18. Python random Data generation Exercise

# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5
import random

print("generating three digit number from 100 to 999 which id divisible by 5")
for i in range(3):
    print(random.randrange(100, 999, 5))


# Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
lottery_tickets_list = []
print("creating 100 random lottery tickets")
# to get 100 ticket
for i in range(100):
    # ticket number must be 10 digit (1000000000, 9999999999)
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))
# pick 2 Luck tickets
winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)


# Exercise 3: Generate 6 digit random secure OTP
import secrets

OTPgenerator = secrets.SystemRandom()

print("six digit random OTP")

otp = OTPgenerator.randrange(100000, 999999)

print("secure OTP is ", otp)


# Exercise 4: Pick a random character from a given String
name = "Milind Mali"

char = random.choice(name)

print(char)


# Exercise 5: Generate random String of length 5
import string

def randomstring(stringLength):
    """gernerate random string of five characters"""

    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(stringLength))

print("random string is ", randomstring(5))


# Exercise 6: Generate a random Password which meets the following conditions
def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)

    random.SystemRandom().shuffle(passwordList)
    password = "".join(passwordList)
    return password

print("password is: ", randomPassword())


# Exercise 7: Calculate multiplication of two random float numbers
num1 = random.random()

num2 = random.uniform(9.5, 99.5)

num3 = num1 + num2

print(num3)


# Exercise 8: Generate random secure token of 64 bytes and random URL
print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))


# Exercise 9: Roll dice in such a way that every time you get the same number
dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))


# Exercise 10: Generate a random date between given start and end dates
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))
