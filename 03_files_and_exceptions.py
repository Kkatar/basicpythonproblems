# 3.files and exceptions

# Exercise 1: Check file is empty or not,Write a program to check if the given file is empty or not
import os

size = os.stat("test file.txt").st_size
if size == 0:
    print("file is empty")
else:
    print("file is not empty")

# Excercise 2:read content from the file
filename = "siddharth.txt"
with open(filename) as f_obj:
    content = f_obj.read()
print(content)

# Excercise 3:# read line by line
filename = "siddharth.txt"
with open(filename) as f_obj:
    for line in f_obj:
        print(line.rstrip())

# storing line to the list
filename = "siddharth.txt"
with open(filename) as f_obj:
    lines = f_obj.readlines()
for line in lines:
    print(line.rstrip())

# Excercise 4:now we will learn about writing to the files
filename = "programming.txt"
with open(filename, 'w') as f:
    f.write("i love machine learning as well")

# Excercise 5: writing multiple line to empty file
with open(filename, 'w') as f:
    f.write("Deep learning is awesome.\n")
    f.write("AI is future\n")

with open(filename, 'a') as f:
    f.write("i love to work with data science projects \n")
    f.write("i love making the application")

# syntax for opening the file using path
filename = "< file path >"
# with open(filename) as f:
#     lines = f.readlines()

# Exercise 6: Write all content of a given file into a new file by skipping line number 5
# read test file
with open("test file.txt", 'r') as fp:
    # read all the lines from the file
    lines = fp.readlines()

# open new file in write mode
with open("test file new.txt", "w") as fp:
    count = 0
    # iterate each line from test file
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            fp.write(line)
        count += 1

# Exercise 7: Read line number 4 from the following file
with open("test file.txt", "r") as fp:
    lines = fp.readlines()
    print(lines[3])

# Excercise 8: Let see handling zero division exceptional error
# print(5/0)

try:
    print(5 / 0)
except ZeroDivisionError:
    print("you cant divide by zero")

filename = "gautam.txt"
try:
    with open(filename) as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"Dear user {filename} may be this file dont exist in directory!")

# Excercise 9:using else block
x = int(input("enter the number: "))
y = int(input("enter the number: "))
try:
    result = x / y
except ZeroDivisionError:
    print("hey you...denominater cant be zero")
else:
    print(result)

# preventing crashes from user input (simple calculator)
print("enter the numbers: ")
print("enter the 'q' to exit")
while True:
    x = input("enter the number:")
    if x == 'q':
        break
    y = input("enter the number:")
    if y == 'q':
        break
    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
        print("bhidu zero se divide nahi kar sakate")
    else:
        print(result)

# Excercise 10: how does finally block work in python
try:
    print(5 / 2)
except ZeroDivisionError:
    print("you cant divide by zero")
finally:
    print("Hip Hip hurray!!")
