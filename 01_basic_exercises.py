# 1. Basic Exercise for Beginners

# Exercise 1: Swap the number without using third varible
x = int(input("enter the first number "))
y = int(input("enter the Second number "))

print(x, y)

x = x + y
y = x - y
x = x - y

print(x, y)


# Exercise 2: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
n = input("enter the number: ")
y = n[::-1]
k = " ".join(y)
print(k)


# Excercise 3: Write a program that will give you the sum of 3 digits
x = int(input("enter three digit number"))
a = x % 10  # we will get last digit
num = x // 10  # integer-divison here we will get first two digit
b = num % 10  # here we will get last digit of two digit number
c = num // 10  # here will get first digit of two digit number
print(a + b + c)


# Excercise 4: Write a program that will reverse a four digit number.Also it checks whether the reverse both number are equal or not
x = int(input("enter the four digit number "))
a = x % 10  # to get last number
num_1 = x // 10  # to get first three numbers
b = num_1 % 10  # this way i will get 2nd last number
num_2 = num_1 // 10  # here will get first two digit number
c = num_2 % 10  # we will get 2 nd number
d = num_2 // 10  # here we will get 1st digit

# formula for reverse
rev = a * 1000 + b * 100 + c * 10 + d
print(rev)

# now let check whether both number are equal or not
if x == rev:
    print(True)
else:
    print(False)


# Excercise 5: Write a program to find the euclidean distance between two coordinates.
import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

x = [x1, y1]
y = [x2, y2]

print("=" * 100)
print("Eucledian distance for given co-ordinate will be", round(math.dist(x, y), 2))


# Excercise 6: Write a program that will tell whether the given number is divisible by 3 & 6.
num = int(input("enter the number "))
if num % 3 == 0 and num % 6 == 0:
    print("the number is divisible by 3 and 6")
else:
    print("the number is not divisible by 3 and 6")


# Excercise 7: Write a program that will take three digits from the user and add the square of each digit.
n = int(input("Enter three digit number: "))
# 123
a = n % 10  # 3
num = n // 10  # 12
b = num % 10  # 2
c = num // 10  # 1
output_value = (a**2) + (b**2) + (c**2)
print(output_value)


# Excercise 8: Write a program that will check whether the number is armstrong number or not.
n = int(input("Enter three digit number: "))
a = n % 10  # 3
num = n // 10  # 12
b = num % 10  # 2
c = num // 10  # 1
if (a**3 + b**3 + c**3) == n:
    print("the number is armstrong number")
else:
    print("the number is not armstrong number")


# Excercise 9:Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.
n = int(input("Enter Four digit number: "))
# 1234
a = n % 10  # 4
num = n // 10  # 123
b = num % 10  # 3
num_1 = num // 10  # 12
c = num_1 % 10  # 2
d = num_1 // 10  # 1

if (a**4 + b**4 + c**4 + d**4) == n:
    print("the number is narcissist number")
else:
    print("the number is not narcissist number")
