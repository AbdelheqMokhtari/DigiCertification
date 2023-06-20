import numpy as np
from sklearn.metrics import mean_squared_error


def calculate_mse(actual, predicted):
    return np.mean((np.array(actual) - np.array(predicted))**2)


def mse_to_percentage(mse, max_possible_mse):
    return (1 - mse / max_possible_mse) * 100


# Example count vectors
vector1 = [25, 39, 26]  # Actual results
vector2 = [22, 33, 26]  # Predicted results

# Calculate the MSE between the count vectors
mse = calculate_mse(vector1, vector2)

# Define the maximum possible MSE
max_possible_mse = np.sum(np.maximum(vector1, vector2))  # Assumes max possible MSE is the sum of maximum counts

# Convert MSE to a similarity percentage
similarity_percentage = mse_to_percentage(mse, max_possible_mse)

# Print the similarity percentage
print("Similarity percentage:", similarity_percentage)