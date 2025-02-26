# Creating variables of each data type
int_var = 10  # Integer
float_var = 20.5  # Float
complex_var = 3 + 4j  # Complex
list_var = [1, 2, 3, 4, 5]  # List
tuple_var = (1, 2, 3, 4, 5)  # Tuple
dict_var = {'name': 'John', 'age': 30}  # Dictionary
set_var = {1, 2, 3, 4, 5}  # Set
bool_var = True  # Boolean

# Printing the type of each variable
print(f"Type of int_var: {type(int_var)}")
print(f"Type of float_var: {type(float_var)}")
print(f"Type of complex_var: {type(complex_var)}")
print(f"Type of list_var: {type(list_var)}")
print(f"Type of tuple_var: {type(tuple_var)}")
print(f"Type of dict_var: {type(dict_var)}")
print(f"Type of set_var: {type(set_var)}")
print(f"Type of bool_var: {type(bool_var)}")

# Converting integer to float and vice versa
int_to_float = float(int_var)
float_to_int = int(float_var)

# Printing the conversion results
print(f"Integer to Float: {int_to_float} (Type: {type(int_to_float)})")
print(f"Float to Integer: {float_to_int} (Type: {type(float_to_int)})")
