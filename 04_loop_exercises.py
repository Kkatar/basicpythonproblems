# 4. Python if else, for loop,while loop and range() Exercises with Solutions

# Exercise 1: Print the sum of the current number and the previous number
prev_num = 0
for i in range(0, 11):
    x = i + prev_num
    prev_num = i
    print(x, end=" ")
print()

# Excercise 2: Write a python program to search a given number from a list
l1 = [4, 5, 6, 2, 3, 9, 1, 4, 5, 6, 3]
n = int(input("enter the number: "))
for i in l1:
    if i == n:
        print("Number exist")
        break
else:
    print("number dont exist")

# Exercise 3:Write a program to check if the given number is a palindrome number.
n = input("enter the number: ")
rev_number = n[::-1]
print(rev_number)
if n == rev_number:
    print("the given number is palindrom")
else:
    print("the given number is not palindrom")

# Exercise 4: Create a new list from a two list using the following condition.
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = []
for i in l1:
    if i % 2 != 0:
        l3.append(i)
for i in l2:
    if i % 2 == 0:
        l3.append(i)
print(l3)

# Exercise 5: Calculate income tax for the given income by adhering to the below rules
n = int(input("enter the number: "))
if n <= 10000:
    print(n)
else:
    a = n - 10000
    b = a - 10000
    c = b * 0.2
    d = c + 1000
    print(d)

# Another way of doing the same
n = int(input("enter the number: "))
a = 10000
b = 10000
c = n - (a + b)
tax = 0
if n <= a:
    tax = 0
elif n > a and n < 20000:
    tax = b * 0.1
else:
    tax = (b * 0.1) + (c * 0.2)
print(tax)

# Exercise 6: Print multiplication table form 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\n")

# Excercise 7: Print all the armstrong numbers in the range of 100 to 1000
armstrong_list = []
for i in range(100, 1000):
    a = i % 10  # 123-->3
    num = i // 10  # 123-->12
    b = num % 10  # --->2
    c = num // 10  # -->1
    if (a**3) + (b**3) + (c**3) == i:
        armstrong_list.append(i)
print(armstrong_list)

# Excercise 8: The current population of a town is 10000.
p = 10000
for i in range(1, 10):
    p = p - 0.1 * p
    print(round(p), end=" ")
print()

# Excercise 9: Write a program to print all the unique combinations of two digits from 1 to 4
# since we have 4 digit there unique combination will be 16
for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            print(i, j)

# Excercise 10:Write a program to print whether a given number is prime number or not
x = int(input("enter the number: "))
new = []
if x == 1:
    print("1 is not prime number")
else:
    for i in range(1, x + 1):
        if x % i == 0:
            new.append(i)
    if len(new) > 2:
        print("it is not a prime number")
    else:
        print("it is prime number ")

# Excercise 11: User will provide 2 numbers you have to find the HCF of those 2 numbers
x = int(input("enter the number: "))
y = int(input("enter the number: "))
x_div = []
y_div = []
for i in range(1, x + 1):
    if x % i == 0:
        x_div.append(i)
for i in range(1, y + 1):
    if y % i == 0:
        y_div.append(i)
comman_list = []
for i in x_div:
    if i in y_div:
        comman_list.append(i)
print("HCF of given two number is ", max(comman_list))

# Excercise 12: User will provide 2 numbers you have to find the by LCM of those 2 numbers
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
if a > b:
    greater = a
else:
    greater = b
while True:
    if (greater % a == 0) and (greater % b == 0):
        LCM = greater
        break
    greater += 1
print(LCM)

# Excercise 13: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
# since sum of all the angle of trianle is 180 deg
a = float(input("1st angle of triangle: "))
b = float(input("2nd angle of triangle: "))
c = float(input("3rd angle of triangle: "))
if (a + b + c) == 180 and a != 0 and b != 0 and c != 0:
    print("yes it can form a triangle")
else:
    print("No it cant form a triangle")

# Excercise 14:Write a program that will determine weather when the value of temperature and humidity is provided by the user.
temp = int(input("enter the value of temp "))
humidity = int(input("enter the value of humidity "))
if temp >= 30 and humidity >= 90:
    print("Hot and Humid")
elif temp >= 30 and humidity < 90:
    print("Hot")
elif temp < 30 and humidity >= 90:
    print("cool and humid")
else:
    print("cool")

# Excercise 15:Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cost = int(input("what is cost of product: "))
sell = int(input("what is sell price of product: "))
if (sell - cost) > 0:
    amount = sell - cost
    print("it is profit by ", amount)
else:
    amount = sell - cost
    print("it is loss by ", amount)

# Excercise 16-Write a program that will give you the in hand salary after deduction of HRA(10%), DA(5%), PF(3%), and tax
salary = int(input("enter the salary amount: "))
if salary in range(500000, 1000000):
    salary = salary - salary * 0.1
elif salary in range(1100000, 2000000):
    salary = salary - salary * 0.2
elif salary > 2000000:
    salary = salary - salary * 0.3
else:
    print("no tax")
print("Salary after tax cutting", salary)
HRA = salary * 0.10  # 63000
DA = salary * 0.05  # 31500
PF = salary * 0.03  # 18900
remain = salary - (HRA + DA + PF)
if remain in range(1000, 99999):
    print("in hand salary after tax/HRA/DA/PF cutting", remain / 1000, "k")
elif remain in range(100000, 9999999):
    print("in hand salary after tax/HRA/DA/PF cutting", remain / 100000, "lakh")
else:
    print("in hand salary after tax/HRA/DA/PF cutting", remain / 10000000, "Cr")

# Excercise 17: Write a menu driven program -
user_input = int(input("""Enter 1 to 'cm' to 'ft'
Enter 2 to 'km' to 'miles'
Enter 3 to 'USD' to 'INR'
Enter 4 to exit """))
if user_input == 1:
    var1 = int(input("enter the value in cm"))
    output = var1 / 30.48
    print(output, 'ft')
elif user_input == 2:
    var2 = int(input("enter the value in km"))
    output = var2 / 1.609
    print(output, 'miles')
elif user_input == 3:
    var3 = int(input("enter the value in usd"))
    output = var3 * 81.80
    print(output, "Inr")
else:
    print("Exit")

# Excercise 18:Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
# number of head--> 1 1
# number of legs--> 4 2
head = int(input("enter the number of heads: "))
legs = int(input("enter the number of legs: "))
if head / legs == 0.25:
    number_of_dogs = legs / 4
    print("there are ", round(number_of_dogs), 'number of dogs')
elif head / legs == 0.5:
    number_of_chicken = legs / 2
    print("there are ", round(number_of_chicken), 'number of chicken')
else:
    print("enter correct numbers")

# Excercise 19: Write a program to find the sum of first n numbers
user_input = int(input("enter the number: "))
x = 0
for i in range(1, user_input + 1):
    x = x + i
print(x)

# Excercise 20: Write a program that can multiply 2 numbers provided by the user without using the * operator
x = int(input("enter the first number: "))  # 2
y = int(input("enter the seconde number "))  # 3
result = 0
for i in range(0, y):
    result = result + x
print(result)

# Excercise 21:Write a program that can find the factorial of a given number provided by the user.
n = int(input("enter the number : "))
factorial = 1
if n < 0:
    print("factorial dont exist for negative number")
elif n == 0:
    print("for zero factorial is always one")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(factorial)

# Excercise 22:print following pattern
n = int(input("enter the number: "))
for i in range(0, n + 1):
    for j in range(0, i):
        print(i, end=" ")
    print("\n")

# Exercise 23: Print First 10 natural numbers using while loop
i = 0
while i < 10:
    for i in range(1, 11):
        print(i, end=" ")

# Exercise 24: Write a program to count the total number of digits in a number using a while loop.
n = input("enter the number: ")
x = list(n)
count = 0
while count < len(x):
    for i in x:
        count += 1
print(count)

# Excercise 25: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.
n = int(input("enter the number: "))
total = 0
avg = 0
count = 0
while True:
    if n != 0:
        total = total + n
        count += 1
        avg = total / count
        n = int(input("print another number: "))
    else:
        print("Thank you")
        break
print("your sum is:", total)
print("your avg is:", round(avg, 2))

# Excercise 26: Write a program to print the first 25 odd numbers
# get me first 25 odd number
# i dont know how many time loop will run--> while loop
flag = 0
i = 1
odd_list = []
while True:
    if i % 2 != 0:
        odd_list.append(i)
        flag = flag + 1
    if flag == 25:
        break
    i = i + 1
print(odd_list)

# Exercise 27: Print the following pattern
n = int(input('enter the number: '))
# 1,2,3,4,5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("\n")

# Excercise 28:
n = int(input("enter the number: "))
num = 1
for i in range(0, n):
    for j in range(0, i + 1):
        print(num, end=" ")
        num = num + 1
    print()

# Excercise 29: Print Pascal Triangle
n = int(input("enter the number: "))
list1 = []
for i in range(0, n):
    temp = []
    for j in range(0, i + 1):
        if j == 0 or j == i:
            temp.append(1)
        else:
            temp.append(list1[i - 1][j] + list1[i - 1][j - 1])
    list1.append(temp)

for i in range(n):
    for j in range(0, n - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print(list1[i][j], end=" ")
    print()

# Exercise 30: Write a program to print multiplication table of a given number
n = int(input("enter the number: "))
for i in range(1, 11):
    x = n * i
    print(x, end=" ")
print()

# Exercise 31: Write a program to display only those numbers from a list that satisfy the following conditions
num = [12, 75, 150, 180, 145, 525, 50]
for i in num:
    if i > 500:
        break
    elif i > 150:
        continue
    else:
        if i % 5 == 0:
            print(i)

# Exercise 32: Print the following pattern (reverse number pattern)
n = int(input('enter the number: '))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("\n")

# Exercise 33: Print list in reverse order using a loop
l1 = [1, 2, 3, 4, 5]
for i in l1[::-1]:
    print(i, end=" ")
print()

# Exercise 34: Display numbers from -10 to -1 using for loop
for i in range(-10, 0):
    print(i, end=" ")
print()

# Exercise 35: Use else block to display a message “Done” after successful execution of for loop
for i in range(0, 5):
    print(i)
else:
    print("done !!")

# Exercise 36: Write a program to display all prime numbers within a range
def prime(n):
    if n <= 1:
        return False
    else:
        l1 = []
        for i in range(1, n + 1):
            if n % i == 0:
                l1.append(i)
        if len(l1) <= 2:
            return True
        else:
            return False

inp1 = int(input("enter the number : "))
inp2 = int(input("enter the number : "))
for i in range(inp1, inp2 + 1):
    if prime(i) == True:
        print(i, end=" ")
print()

# Exercise 37: Display Fibonacci series up to 10 terms
n = int(input("enter the number: "))
num1 = 0
num2 = 1
print(num1, end=" ")
print(num2, end=" ")
for i in range(0, n):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3, end=" ")
print()

# Exercise 38: Write a program to use the loop to find the factorial of a given number.
n = int(input("enter the number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

# Exercise 39: Reverse a given integer number
n = int(input("enter the number: "))
x = str(n)
x = list(x)[::-1]
z = int("".join(x))
print(z)

# Exercise 40: Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list[1::2])

# Exercise 41: Write a program to print the cube of all numbers from 1 to a given number
n = 6
for i in range(1, 7):
    x = pow(i, 3)
    print("current number is {} and the cube is {}".format(i, x))

# Exercise 42: Write a program to calculate the sum of series up to n term.
n = 5
x = 2
result = 0
for i in range(1, 6):
    y = str(x) * i
    z = int("".join(y))
    result = result + z
print(result)

# Exercise 43: Print downward Half-Pyramid Pattern with Star (asterisk)
n = int(input("enter the number : "))
for i in range(n + 1, 1, -1):
    for j in range(1, i):
        print("*", end=" ")
    print("\n")

# Exercise 44: print right half side of the pyramid
n = int(input("enter the number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("\r")

# Excercise 45: Centered pyramid pattern
n = 5
for i in range(0, n):
    for j in range(0, n - i):
        print(end=" ")
    for k in range(0, i + 1):
        print("*", end=" ")
    print()

# Exercise 46: Write a program to print the following start pattern using the for loop
n = int(input("enter the number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("\n")
for i in range(n - 1, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print("\n")
