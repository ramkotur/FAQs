import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)


# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Create a 3D Array
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(3):
    for l in range(3):
        print(str(a[i,l]))

# Element-wise addition
arr_sum = arr1 + 10
print("Element-wise addition:", arr_sum)

# Element-wise multiplication
arr_mul = arr1 * 2
print("Element-wise multiplication:", arr_mul)


# Slicing a 1D array
slice1 = arr1[1:4]
print("Sliced 1D Array:", slice1)

# Slicing a 2D array
slice2 = arr2[:, 1:3]
print("Sliced 2D Array:\n", slice2)


# Reshape a 1D array to a 2D array
reshaped_arr = arr1.reshape((1, 5))
print("Reshaped Array:\n", reshaped_arr)


# Calculate mean
mean_val = np.mean(arr1)
print("Mean:", mean_val)

# Calculate standard deviation
std_val = np.std(arr1)
print("Standard Deviation:", std_val)

# Create two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Perform matrix multiplication
matrix_product = np.dot(matrix1, matrix2)
print("Matrix Product:\n", matrix_product)


# Create an array of zeros
zeros_arr = np.zeros((3, 3))
print("Array of Zeros:\n", zeros_arr)

# Create an array of ones
ones_arr = np.ones((2, 4))
print("Array of Ones:\n", ones_arr)

# Create an identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)


