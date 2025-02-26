# Function to classify a number as even or odd
def classify_number(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Ask the user for an integer input
user_input = int(input("Enter an integer: "))

# Check if the number is even or odd
result = classify_number(user_input)
print(f"The number {user_input} is {result}.")

# Generate and print a list of even numbers from 1 to 50 using a for loop
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("Even numbers from 1 to 50:", even_numbers)

# Use a while loop to print numbers from 10 down to 1
print("Numbers from 10 down to 1:")
num = 10
while num > 0:
    print(num)
    num -= 1
