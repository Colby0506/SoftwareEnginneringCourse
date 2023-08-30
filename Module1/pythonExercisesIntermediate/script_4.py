def get_valid_input():
    while True:
        try:
            value = int(input("Enter an integer: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

input_count = 5
numbers = []

for i in range(input_count):
    valid_input = get_valid_input()
    numbers.append(valid_input)

total_sum = sum(numbers)
print("Sum of the entered integers:", total_sum)