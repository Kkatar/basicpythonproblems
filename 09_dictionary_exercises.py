# 9. Python Dictionary Exercise with Solutions

# Excercise 1:Get the only keys of dictionary
dicti = {"name": "Milind", "Age": 34}
# to get list of all the keys
print(dicti.keys())

# Exercise 2: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = zip(keys, values)
result = dict(my_dict)
print(result)

# Exercise 3: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)

# another way of achieving same is:
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

# Exercise 4: Print the value of key ‘history’ from the below dict
sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
print(sampleDict["class"]["student"]["marks"]["history"])

# Exercise 5: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = dict.fromkeys(employees, defaults)
print(result)
print("=" * 100)
print("Details of kelly: ", result["Kelly"])

# Exercise 6: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
result = dict()
for k in keys:
    result.update({k: sample_dict[k]})
print(result)

# using dictionary comprehension
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
new_dict = {k: sample_dict[k] for k in keys}
print(new_dict)

# Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("200 is present in given dict")

# Exercise 8: Rename key of a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
# list1=[]
print(min(sample_dict, key=sample_dict.get))

# Exercise 10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict["emp3"]["salary"] = 8500
print(sample_dict)
