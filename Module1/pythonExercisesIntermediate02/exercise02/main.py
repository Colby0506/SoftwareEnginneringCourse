import random
import time

# Function to compute the nth term of the Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Generate a random number between 15 and 35 inclusive
n = random.randint(15, 35)

# Measure the time it takes to compute the Fibonacci sequence
start_time = time.time()
result = fibonacci(n)
end_time = time.time()

# Print the result and the time taken
print(f"The {n}th term of the Fibonacci sequence is: {result}")
print(f"Time taken: {end_time - start_time:.6f} seconds")