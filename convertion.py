# Converting string to integer
age_str = "25"
age_int = int(age_str)
print(f"age:{age_int}")\

# Converting string to float
height_str = "1.75"
height_float = float(height_str)
print(f"height:{height_float}")

# Converting to boolean
print(bool(0))          # False
print(bool(42))         # True
print(bool(""))         # False
print(bool("Hello"))    # True

# converting boolean to integer
print(int(True))        # 1
print(int(False))       # 0


# Putting it all together
# Data types and operators practice

# Get user input
name = input("Enter your name: ")
age_str = input("Enter your age: ")
height_str = input("Enter your height in meters: ")

# Convert input to appropriate types
age = int(age_str)
height = float(height_str)

# Perform calculations
# You may need to change the year to the current year
birth_year = 2025 - age
is_adult = age >= 18

# Create output string
output = f"""
Name: {name}
Age: {age}
Height: {height:.2f} meters
Birth Year: {birth_year}
Is Adult: {is_adult}
"""

# Print the result
print(output)

# Bonus: String manipulation
uppercase_name = name.upper()
name_length = len(name)

print(f"Your name in uppercase: {uppercase_name}")
print(f"Your name has {name_length} characters")