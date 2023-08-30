def count_letters(input_string):
    letter_count = {}
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    return letter_count

user_input = input("Enter a string: ")
result_dict = count_letters(user_input)
print(result_dict)