import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.metrics import jaccard_score, accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error


def calculate_mse(actual, predicted):
    return np.mean((np.array(actual) - np.array(predicted))**2)


results = pd.read_csv('CCLS .csv')
predicted = pd.read_csv('Prediction CCLS .csv')
similarity = []
euclidean = []
jaccard = []
mse_percentage = []

for index, row in results.iterrows():
    vector_result = row[1:].values
    vector_result = vector_result.tolist()
    predicted_result = predicted.iloc[index, 1:].values
    predicted_result = predicted_result.tolist()

    # Calculate the total of Ble dur
    total = sum(vector_result[:4])
    vector_result[:4] = [total]
    # total = sum(predicted_result[:4])
    # predicted_result[:4] = [total]
    vector_result.pop()
    vector_result.pop()
    predicted_result.pop()
    # calculate the similarity between the real values and predictable values
    # print(vector_result)
    # print(predicted_result)
    sim = cosine_similarity([vector_result], [predicted_result])
    similarity.append(sim[0][0])
    vector1 = np.array(vector_result)
    vector2 = np.array(predicted_result)

    # Calculate the MSE
    mse = mean_squared_error(vector_result, predicted_result)

    # print(f"The Mean Squared Error is {mse}")
    max_possible_mse = mean_squared_error(vector_result, [0, 0, 0, 0, 0])
    percentage = (1 - mse / max_possible_mse) * 100
    # print(f"The Mean Squared Percentage is {percentage}")
    mse_percentage.append(percentage)

    # Calculate the MSLE
    msle = mean_squared_log_error(vector_result, predicted_result)

    # Convert MSLE to a similarity score
    similarity_score = (1 - msle) * 100

    # print(f"The similarity score is {similarity_score}%")

similarity_avg = sum(mse_percentage) / len(mse_percentage)
print("the average similarity of the dataset = ", similarity_avg)

# similarity_percentage = sum(percentage) / len(percentage)
# print("the average similarity of MSE = {:.2%}".format(similarity_percentage))

# euclidean_distance_avg = sum(euclidean)/len(euclidean)
# print("the average similarity of euclidean = {:.2%}".format(euclidean_distance_avg))

# jaccard_avg = sum(jaccard)/len(jaccard)
# print("the average similarity of jaccard = {:.2%}".format(jaccard_avg))