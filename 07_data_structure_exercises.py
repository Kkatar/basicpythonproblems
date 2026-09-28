# 7. Python Data Structure Exercise for Beginners

# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
for i in l1[1::2]:
    l3.append(i)
for i in l2[0::2]:
    l3.append(i)
print(l3)

# Exercise 2: Remove and add item in a list
list1 = [34, 54, 67, 89, 11, 43, 94]
list1.pop(4)
list1.insert(2, 11)
list1.append(11)
print(list1)

# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
l1 = [11, 49, 8, 23, 14, 12, 78, 45, 89]
n = 3
output = [l1[i:i + n][::-1] for i in range(0, len(l1), n)]
print(output)

# Exercise 4: Count the occurrence of each element from a list
list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count = dict()
for i in list1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
intersection = first_set.intersection(second_set)
print(intersection)
for i in intersection:
    first_set.remove(i)
print(first_set)

# Exercise 6: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print("first set is subset of second set:\n", first_set.issubset(second_set))
print("second set is subset of first set:\n", second_set.issubset(first_set))
print("first set is superset of second set:\n", first_set.issuperset(second_set))
print("second set is superset of first set:\n", second_set.issuperset(first_set))
if first_set.issubset(second_set):
    first_set.clear()
if second_set.issubset(first_set):
    second_set.clear()
print("first set:\n", first_set)
print("second set:\n", second_set)

# Exercise 7: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
# will modify the original list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print(roll_number)

# Exercise 8: Get all values from the dictionary and add them to a list but don’t add duplicates
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
speed_list = []
for value in speed.values():
    if value not in speed_list:
        speed_list.append(value)
print(speed_list)

# Exercise 9: Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
list1 = set(sample_list)  # removed all the duplicates
tuple1 = tuple(list1)
print("Unique element in the sample list:\n", tuple1)
print("Maximum number in the sample list:\n", max(tuple1))
print("Minimun number in the sample list:\n", min(tuple1))
