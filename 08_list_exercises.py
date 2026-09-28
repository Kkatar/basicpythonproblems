# 8. Python List exercise with solutions

# Excercise: 1 Write a python program to find the max item from a list without using the max function
l1 = [4, 6, 2, 8, 1]
l1.sort(reverse=True)
print(l1[0])

# Excercise 2 Find the reverse of a number provided by the user(any number of digit)
n = int(input("enter the number: "))
digit_list = list(map(int, str(n)))
digit_list = digit_list[::-1]
num = int("".join(map(str, digit_list)))
print(num)

# Excercise 3 Take a number from the user and find the number of digits in it.
n = int(input("enter the number: "))
digit_list = list(map(int, str(n)))
print(digit_list)
print(len(digit_list))

# Exercise 4: Write a python program to remove all the duplicates from a list
l1 = [1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

# Exercise 5: Reverse a list in Python
list1 = [100, 200, 300, 400, 500]
print(list1[::-1])
# or you can also use "reverse()" function

# Exercise 6: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

# Exercise 7: Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
new = []
for i in numbers:
    x = pow(i, 2)
    new.append(x)
print(new)

# same using list comprehenssion
result = [pow(x, 2) for x in numbers]
print(result)

# Exercise 8: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        print(i + j)

# using list comprehension
result = [i + j for i in list1 for j in list2]
print(result)

# Exercise 9: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)

# Exercise 10: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
result = list(filter(lambda x: x != "", list1))
print(result)

# Exercise 11: Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# Exercise 12: Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

# Exercise 13: Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
x = list1.index(20)
list1[x] = 200
print(list1)

# Exercise 14: Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)

# Excercise 15 :Write a program that can perform union and intersection on 2 given list.
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
uni = []
inter = []
for i in l1:
    if i in l2:
        inter.append(i)
print(inter)

for i in l1:
    if i not in uni:
        uni.append(i)

for i in l2:
    if i not in uni:
        uni.append(i)
print(uni)

# Excercise 16: break down the list into equal number of chucks
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
chunk = 3
output = [l1[i:i + chunk] for i in range(0, len(l1), chunk)]
print(output)

# Excercise 17: logic for quickly swap the first and last number of the list
l1 = [1, 2, 3, 4, 5]
temp = l1[-1]
l1[-1] = l1[0]
l1[0] = temp
print(l1)

# Excercise 18: what is easiest way to shuffle the list
from random import shuffle

list1 = ["Milind", "Kanchan", "Rohit", "Shashi"]
shuffle(list1)
print(list1)

# Excercise 19 create lambda function for the sum of all the elements in the list
l1 = [5, 8, 10, 20, 50, 100]
from functools import reduce

result = reduce(lambda x, y: x + y, l1)
print(result)
