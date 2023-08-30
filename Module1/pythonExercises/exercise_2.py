user_input = input("Enter a string: ")

lowercase_letters = ""
uppercase_letters = ""
for char in user_input:
    if char.islower():
        lowercase_letters += char
    elif char.isupper():
        uppercase_letters += char

result_string = lowercase_letters + uppercase_letters
print("Modified string:", result_string)