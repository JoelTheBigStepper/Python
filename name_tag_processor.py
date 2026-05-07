first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
full_name = f"{first_name} {last_name}"
adjusted_name = full_name.slice()
print(len(full_name))
print(full_name.upper())
print(full_name.replace(" ", "_"))
print(adjusted_name)