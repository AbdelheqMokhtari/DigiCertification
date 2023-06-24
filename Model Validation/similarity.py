import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Read the CSV file
results = pd.read_csv('CCLS.csv')
predicted = pd.read_csv('CCLS_predicted.csv')

# Retrieve the first row as a vector
first_row = results.iloc[1, 1:].values
first_row = first_row.tolist()
first_row_predicted = predicted.iloc[1, 1:].values
first_row_predicted = first_row_predicted.tolist()

# Calculate the total of Ble dur
total = sum(first_row[:4])
first_row[:4] = [total]
total = sum(first_row_predicted[:4])
first_row_predicted[:4] = [total]

# Print the first row
print(first_row)

# Calculate the similarity between two vectors
# vector1 = vectors['Vitron']
# vector2 = vectors['Bousselam']
similarity = cosine_similarity([first_row], [first_row_predicted])
# Perform desired operations with the row's data
# print(f"Similarity between Vitron and Bousselam: {similarity[0][0]}")
similarity = similarity.tolist()

print(similarity[0][0])