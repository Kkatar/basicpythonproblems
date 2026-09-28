# 6. Python string Excercise with solutions

# Exercise 1: Return the count of a given substring from a string
sentence = "radha is most beutiful,radha is queen of vraj,radha is most beloved to govind"
x = sentence.count("radha")
print(x)

# Exercise 2: Print characters from a string that are present at an even index number
string = input("enter the text: ")
x = list(string)
print(string)
for i in x[0::2]:
    print(i, end=" ")
print()

# Exercise 3: Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove(word, n):
    x = len(word)
    p = list(word)
    for i in p:
        if n <= x:
            z = word[n:]
    print(z)

remove("pynative", 2)

# Exercise 4 1A: Create a string made of the first, middle and last character
name = "james"
a = name[0]
print(a)
c = name[-1]
print(c)
l = len(name)
x = int(l // 2)
b = name[x]
print(b)
print("".join([a, b, c]))

# Exercise 4B: Write a program to create a new string made of the middle three characters of an input string.
name = "JaSonAy"
l = len(name)
if l % 2 == 0:
    print("not possible")
else:
    c = l // 2
    x = name[c - 1]
    y = name[c]
    z = name[c + 1]
    result = "".join([x, y, z])
    print(result)

# Excercise 5 :Count the frequency of a particular character in a provided string.
a = input("enter the text: ")
b = input("enter the character: ")
count = 0
for i in a:
    if i in b:
        count = count + 1
print("frequency of searched character is ", count, "times")

# Excercise 6:Find the index position of a particular character in another string.
a = input("enter the text: ")
b = input("enter the character: ")
print(a.index(b))

# Excercise 7: Write a program which can remove a particular character from a string.
a = input("enter the string: ")
b = input('enter the character you want to remove: ')
a = a.replace(b, "")
print(a)

# Exercise 8: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
l = len(s1)
mid = l // 2
f = s1[:mid]
s = s1[mid:]
s3 = f + s2 + s
print(s3)

# Exercise 9: Create a new string made of the first, middle, and last characters of each input string
def unite(s1, s2):
    l1 = len(s1) // 2
    a = s1[0]
    b = s1[l1]
    c = s1[-1]

    l2 = len(s2) // 2
    x = s2[0]
    y = s2[l2]
    z = s2[-1]

    result = "".join([a, x, b, y, c, z])
    return result

print(unite("america", "japan"))

# Exercise 10: Arrange string characters such that lowercase letters should come first
string = "PyNaTive"
cap = list(string.upper())
sma = list(string.lower())
new = []
l1 = list(string)
for i in l1:
    if i in sma:
        new.append(i)
for i in l1:
    if i in cap:
        new.append(i)
result = "".join(new)
print(result)

# another way of doing the same thing
given = "PyNaTive"
x = given.upper()
l1 = []
for i in given:
    if i not in x:
        l1.append(i)
for i in given:
    if i in x:
        l1.append(i)
result = "".join(l1)
print(result)

# Exercise 11: Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
l1 = list(str1)
char = 0
digit = 0
special_char = 0
for i in l1:
    if i.isalpha() == True:
        char += 1
    elif i.isdigit() == True:
        digit += 1
    else:
        special_char += 1
print("char", char)
print("digit", digit)
print("special_char", special_char)

# Exercise 12: Create a mixed String using the following rules
s1 = "ABC"
s2 = "xyz"
a = s1[0]
b = s1[len(s1) // 2]
c = s1[-1]

x = s2[0]
y = s2[len(s2) // 2]
z = s2[-1]

result = "".join([a, z, b, y, c, x])
print(result)

# Exercise 13: String characters balance Test
s1 = "Yn"
s2 = "PYnative"
count = 0
for i in s1:
    if i in s2:
        count += 1
if len(s1) == count:
    print("s1 and s2 are balanced")
else:
    print("s1 and s2 are not balanced")

# Exercise 14: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
str2 = str1.upper()
print(str2)
print(str2.count("USA"))

# Excercise 15 Write a python program to convert a string to title case without using the title()
a = input("enter the title: ")
b = a.split()
r = ''
for i in b:
    r = r + i.capitalize() + " "
print(r)

# Exercise 16: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
str2 = list(str1)
total = 0
counter = 0
for i in str2:
    if i.isdigit() == True:
        total = total + int(i)
        counter += 1
print("sum of digits in the given string is ", total)
print("avg of digits in the given string is ", round(total / counter, 2))

# Exercise 17: Reverse a given string
str1 = "PYnative"
print(str1[::-1])

# Exercise 18: Find the last position of a given substring
str1 = "Milind is a data scientist who knows Python. Milind works at google."
print(str1.rfind("Milind", 2))

# Exercise 19: Split a string on hyphens
str1 = "Emma-is-a-data-scientist"
str2 = str1.split("-")
for i in str2:
    print(i)

# Exercise 20: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for i in str_list:
    if i == "" or i == None:
        str_list.remove(i)
print(str_list)

# Exercise 21: Remove special symbols / punctuation from a string
sentence = "/*Jon is @developer & musician"
import re

clean_sentence = re.sub('[^A-Za-z0-9\\s]+', "", sentence)
print(clean_sentence)

# Exercise 22: Removal all characters from a string except integers
str1 = 'I am 26 years and 10 months old'
str2 = str1.split()
new = []
for i in str2:
    if i.isdigit() == True:
        new.append(i)
print("".join(new))

# Exercise 23: Find words with both alphabets and numbers
# isalnum()
str1 = "Emma253 is Data scientist50000 and AI Expert"
str2 = str1.split()
new = []
for i in str2:
    for j in i:
        if j.isdigit() == True:
            if i not in new:
                new.append(i)
print(new[:])

# Exercise 24: Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
import string

for i in string.punctuation:
    if i in str1:
        str1 = str1.replace(i, "#")
print(str1)

# Exercise:25 extract the email service provider name
emaillist = ["KSR@datavizion.com", "mymail@yahoo.com", "milindmali@google.com", "snehal@healthcare.com"]
for i in emaillist:
    i = i.replace("@", ".").split(".")
    print(i[1])

# Exercies 26: extract all the emailid for the given string
string = "Hi my name is Govind Das and my mail id is milindmali108@gmail.com and my org mail id is milind@google.com"
new = list(string.split())
for i in new:
    if ".com" in i:
        print(i)

# Excercise 27: write progrme to count the number of vowels in the string
string = "Milind Dattatray Mali"
vowel = "AEIOUaeiou"
count = 0
for i in string:
    if i in vowel:
        count += 1
print(count)
