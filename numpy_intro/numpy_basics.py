# Define some numbers
int_num = 10
float_num = 15.5
complex_num = 3 + 4j

# Perform basic operations
sum_result = int_num + float_num  # Adding integer and float
diff_result = float_num - int_num  # Subtracting int from float
prod_result = int_num * 2  # Multiplying int by 2
quot_result = float_num / int_num  # Dividing float by int

# Print the results
print("Sum of integer and float:", sum_result)
print("Difference between float and integer:", diff_result)
print("Product of integer and 2:", prod_result)
print("Quotient of float divided by integer:", quot_result)

# List of numbers
numbers = [5, 10, 15, 20, 25]

# Calculate the square of each number using a for loop
squares = [num ** 2 for num in numbers]
print("Squares of numbers:", squares)

# Find the sum of the numbers in the list
list_sum = sum(numbers)
print("Sum of the numbers in the list:", list_sum)

# Find the maximum and minimum numbers in the list
max_num = max(numbers)
min_num = min(numbers)
print("Maximum number in the list:", max_num)
print("Minimum number in the list:", min_num)
