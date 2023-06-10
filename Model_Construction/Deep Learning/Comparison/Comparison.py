import json

import matplotlib.pyplot as plt


def load_json(file_path):
    with open(file_path, 'r') as file:
        history = json.load(file)
    return history


def plot_multiple_training_histories(histories):
    # Set the colors and line styles for each history
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    line_styles = ['-', '--', '-.', ':']

    # Plot loss
    plt.figure(figsize=(8, 6))
    for i, history in enumerate(histories):
        loss = history['loss']
        color = colors[i % len(colors)]
        line_style = line_styles[i % len(line_styles)]
        plt.plot(loss, label='Loss ' + str(i+1), color=color, linestyle=line_style)

    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.legend()
    plt.show()

    # Plot accuracy
    plt.figure(figsize=(8, 6))
    for i, history in enumerate(histories):
        accuracy = history['accuracy']
        color = colors[i % len(colors)]
        line_style = line_styles[i % len(line_styles)]
        plt.plot(accuracy, label='Accuracy ' + str(i+1), color=color, linestyle=line_style)

    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Training Accuracy')
    plt.legend()
    plt.savefig('training_accuracy.png')
    plt.show()


# Usage:
# history1 = load_json('history/CNCC/Resnet18_epochs50_history.json')  # Replace with the appropriate file paths
# history2 = load_json('history/CNCC/Resnet50_epochs50_history.json')
# plot_multiple_training_histories([history1, history2])

# Specify the path to the JSON file
json_file = 'classification_report.json'

classification_rapport = load_json("classification rapport/CNCC/ResNet50/classification_report.json")


# Access the accuracy value
accuracy = classification_rapport['accuracy']

print('Accuracy:', accuracy)

