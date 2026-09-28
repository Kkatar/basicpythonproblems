# 15. Python NumPy Exercise

# Excercise 1:the max item of each row of a matrix.
import numpy as np

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = np.asarray(x)
print(y)
print(y.max())

# Exercise 2: Create a 4X2 integer array and Prints its attributes
firstArray = np.empty([4, 2], dtype=np.uint16)
print(firstArray)
print("shape of the array is: ", firstArray.shape)
print("dimension of the array is: ", firstArray.ndim)
print("itemsize of each element in array is:", firstArray.itemsize)

# Exercise 3: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
my_array = np.arange(100, 200, 10)
my_array = my_array.reshape(5, 2)
print(my_array)

# Exercise 4: Following is the provided numPy array. Return array of items by taking the third column from all rows
sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
# print(sampleArray)
new_array = sampleArray[..., 2]
print(new_array)

# Exercise 5: Return array of odd rows and even columns from below numpy array
sampleArray = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
# print(sampleArray)
new_array = sampleArray[1::2, ::2]
print(new_array)

# Exercise 6: Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element
arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])
# print(arrayOne)
# print(arrayTwo)
result_array = arrayOne + arrayTwo
print(result_array)
final_output = pow(result_array, 2)
print(final_output)

# Exercise 7: Split the array into four equal-sized sub-arrays
new_array = np.arange(10, 34, 1)
new_array = new_array.reshape(8, 3)
print(new_array)
# now to divide array into 4 equal division
subarray = np.split(new_array, 4)
print("=" * 100)
print(subarray)

# Exercise 8: Sort following NumPy array
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)
# sorting original array by second row
sortArrayByRow = sampleArray[:, sampleArray[1, :].argsort()]
print("Sorting Original array by secoond row")
print(sortArrayByRow)
print("Sorting Original array by second column")
sortArrayByColumn = sampleArray[sampleArray[:, 1].argsort()]
print(sortArrayByColumn)

# Exercise 9: Print max from axis 0 and min from axis 1 from the following 2-D array.
import numpy

print("Printing Original array")
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)
minOfAxisOne = numpy.amin(sampleArray, 1)
print("Printing amin Of Axis 1")
print(minOfAxisOne)
maxOfAxisOne = numpy.amax(sampleArray, 0)
print("Printing amax Of Axis 0")
print(maxOfAxisOne)

# Exercise 10: Delete the second column from a given array and insert the following new column in its place.
print("Printing Original array")
sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(sampleArray)
print("Array after deleting column 2 on axis 1")
sampleArray = numpy.delete(sampleArray, 1, axis=1)
print(sampleArray)
arr = numpy.array([[10, 10, 10]])
print("Array after inserting column 2 on axis 1")
sampleArray = numpy.insert(sampleArray, 1, arr, axis=1)
print(sampleArray)
