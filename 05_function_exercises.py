# 5. Python Functions Exercise

# Exercise 1: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    result = pow(base, exp)
    print(result)

exponent(10, 2)


# Exercise 2: Write a program to create a function that takes two arguments, name and age, and print their value.
def biodata(name, age):
    print("Name of the person is {} and age is {}".format(name, age))

biodata("Milind", 26)


# Exercise 3: Write a function to return True if the first and last number of a given list is same.
l1 = [1, 2, 3, 4, 5, 1]
num1 = l1[0]
num2 = l1[-1]

def xyz(list):
    if num1 == num2:
        return True
    else:
        return False

print(xyz(l1))


# Exercise 4:Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
num1 = int(input("enter the number: "))
num2 = int(input("enter the number: "))

def mul_sum_int(num1, num2):
    # calculate product of two number
    mul = num1 * num2
    total = num1 + num2
    # checking if product is less than 1000
    if mul <= 1000:
        return mul
    else:
        return total

print(mul_sum_int(num1, num2))


# Exercise 5: Create a function with variable length of arguments
def inputs(*num):
    return num

print(inputs(45, 67, 78))
print(inputs(34, 56))


# Excercies 6:collecting arbitrary number of arguments
def make_pizza(size, *toppings):
    print(f"making {size} pizza")
    print("toppings: ")
    for i in toppings:
        print(i)

make_pizza("small", "butter")
make_pizza("medium", "amli", "paeri", "dijvoe")


# Excercise 7: collecting arbitrary number of keyword arguments
def build_profile(fname, lname, **userinfo):
    # build dictionary
    profile = {"first Name": fname, "Last Name": lname}
    for key, value in userinfo.items():
        profile["key"] = value
    return profile

print(build_profile("milind", "mali"))
print(build_profile("milind", "mali", age=26, Loc="Pune"))


# Exercise 8: Return multiple values from a function
def add_sub(n1, n2):
    x1 = n1 + n2
    x2 = n1 - n2
    return x1, x2

print(add_sub(40, 10))


# Exercise 9: Create a function with a default argument
def show_employee(name, salary="9000"):
    print("name of employee is {} and his\\her salary is {}".format(name, salary))

show_employee("milind", 78686)
show_employee("Vishal")


# Exercise 10: Create an inner function to calculate the addition in the following way
def outerfunc(n1, n2):
    def innerfunc(n1, n2):
        return n1 + n2
    add = innerfunc(n1, n2)
    return add + 5

print(outerfunc(5, 10))


# Exercise 11: Create a recursive function
# A] Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def addition(num):
    if num == 0:
        return 0
    else:
        return num + addition(num - 1)

print(addition(10))

# B] Write a program to create a recursive function to calculate the factorial of numbers from 0 to 10.
def factorial(num):
    if (num == 1):
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))


# Exercise 12: Assign a different name to function and call it through the new name
def display_student(name, age):
    print("name of student {} and his age is {}".format(name, age))

show_student = display_student
show_student("Mihir", 29)


# Exercise 13: Generate a Python list of all the even numbers between 4 to 30
for i in range(4, 31):
    if i % 2 == 0:
        print(i, end=" ")
print()
# another way
print(list(range(4, 31, 2)))


# Exercise 14: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2, 65]
y = 0
for i in x:
    if i > y:
        y = i
print(y)
print(max(x))


# Excercise 15: first 25 prime number
# first we will write code for getting prime number
a = 23
new = []
for i in range(1, a + 1):
    if a % i == 0:
        new.append(i)

if len(new) > 2:
    print("it's not a prime number")
else:
    print("it's prime number")

# to get first 25 numbers
def is_prime(x):
    new = []
    if x <= 1:
        return False
    else:
        for i in range(1, x + 1):
            if x % i == 0:
                new.append(i)
        if len(new) <= 2:
            return True
        else:
            return False

count = 0
num = 2
while count < 25:
    if is_prime(num) == True:
        print(num, end=" ")
        count += 1
    num += 1
print()


# Excercise 16: Print the first 20 numbers of a Fibonacci series
n = int(input("enter the number: "))

def fibonacci(n):
    a = 0
    b = 1
    count = 0
    if n <= 0:
        print("You can enter only Positive integer values")
    elif n == 1:
        print(a)
    else:
        while count < n:
            print(a, end=' ')
            c = a + b
            a = b
            b = c
            count += 1

fibonacci(n)
print()


# Excercise 17: Write the logic for strong number strong number in python
# 145-->1!+4!+5!
n = 145
total = 0

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for i in str(n):
    x = fact(int(i))
    total += x

if n == total:
    print("It is strong number")
else:
    print("it is not a strong number")


# Excercise 18: write logic to know whethe given number is perfect number or not
from functools import reduce

n = 28
l1 = []
for i in range(1, n):
    if n % i == 0:
        l1.append(i)

result = reduce(lambda x, y: x + y, l1)
if n == result:
    print("perfect number")
else:
    print("Not perfect number")
