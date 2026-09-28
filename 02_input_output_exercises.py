# 2. python input and output exercise

# Exercise 1: Accept numbers from a user
name = input("enter the name: ")

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name ** Is ** James”
print("name", "is", "james", sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting
number = 12
print(oct(number)[-2:])

# Exercise 4: Display float number with 2 decimal places using print()
num = 56.87547
y = float(round(num, 2))
print(y)

# Excercise 5:Print all factors of a given number provided by the user.
n = int(input("enter the number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

# Exercise 6: Accept a list of 5 float numbers as an input from the user
l1 = []
while len(l1) < 5:
    n = float(input("enter the number: "))
    l1.append(n)
print(l1)

# Exercise 7: Accept any three string from one input() call
inp = input("enter the three names with keeping space in between: ")
sep = inp.split()
# print(sep)
name1 = sep[0]
name2 = sep[1]
name3 = sep[2]
print(name1)
print(name2)
print(name3)

# Exercise 8: Format variables using a string.format() method.
totalmoney = 1200
quantity = 4
price = 450
print("i have {} dollars so i can buy {} football for {} dollars".format(totalmoney, quantity, price))

# Excercise 9: Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
P = float(input("principle amount: "))
R = float(input("Rate of interest: "))
T = int(input("for the time period: "))
Simple_interest = (P * R * T) / 100
print(Simple_interest)
total_due = P + Simple_interest
print("Total due amount will need to pay wll be ", total_due)

# Excercise 10: Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
rad = float(input("enter the radius of cylinder in cm "))
ht = float(input("enter the height of cylinder in cm "))
vol = 3.142 * (rad**2) * ht
litr = vol / 1000
cost = litr * 40
print("Volume of cylinder will be ", vol)
print("How much milk we can carry in this cylinder ", litr, 'ltr')
print("this cost of that milk will be", cost)
