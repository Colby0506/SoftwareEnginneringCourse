import numpy as np

# Generate a NumPy array of 10 random floats between 0 and 1
random_floats = np.random.rand(10)

# Calculate and print the mean, median, and standard deviation
mean_value = np.mean(random_floats)
median_value = np.median(random_floats)
std_deviation = np.std(random_floats)

print(f"Random Floats: {random_floats}")
print(f"Mean: {mean_value:.4f}")
print(f"Median: {median_value:.4f}")
print(f"Standard Deviation: {std_deviation:.4f}")