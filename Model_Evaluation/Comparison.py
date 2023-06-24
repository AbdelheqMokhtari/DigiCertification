import json
import matplotlib.pyplot as plt


def load_json(file_path):
    with open(file_path, 'r') as file:
        history = json.load(file)
    return history


def plot_multiple_training_histories(histories):
    # Set the colors and line styles for each history
    # colors = ['blue', 'red', 'green', 'orange', 'purple', 'yellow', 'cyan']
    colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
    # line_styles = ['-', '--', '-.', ':']
    architectures = ['DenseNet121', 'DenseNet169', 'DenseNet201', 'InceptionResNetV2', 'ResNet50', 'VGG16', 'VGG19']

    # Plot loss
    plt.figure(figsize=(8, 6))
    for i, history in enumerate(histories):
        loss = history['loss']
        color = colors[i % len(colors)]
        # line_style = line_styles[i % len(line_styles)]
        plt.plot(loss, label=architectures[i], color=color)

    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.legend()
    plt.savefig('CNCC/CNCC_Training_Loss.png')
    plt.show()

    # Plot accuracy
    plt.figure(figsize=(8, 6))
    for i, history in enumerate(histories):
        accuracy = history['accuracy']
        color = colors[i % len(colors)]
        # line_style = line_styles[i % len(line_styles)]
        # plt.plot(accuracy, label='Accuracy ' + str(i+1), color=color, linestyle=line_style)
        plt.plot(accuracy, label=architectures[i], color=color)

    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Training Accuracy')
    plt.legend()
    plt.savefig('CNCC/CNCC_Training_accuracy.png')
    plt.show()

    # Plot val accuracy
    plt.figure(figsize=(8, 6))
    for i, history in enumerate(histories):
        accuracy = history['val_accuracy']
        color = colors[i % len(colors)]
        # line_style = line_styles[i % len(line_styles)]
        plt.plot(accuracy, label=architectures[i], color=color)

    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Validation Accuracy')
    plt.legend()
    plt.savefig('CNCC/CNCC_Validation_Accuracy.png')
    plt.show()

    # Plot accuracy
    plt.figure(figsize=(8, 6))
    for i, history in enumerate(histories):
        accuracy = history['val_loss']
        color = colors[i % len(colors)]
        # line_style = line_styles[i % len(line_styles)]
        plt.plot(accuracy, label=architectures[i], color=color)

    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Validation Error')
    plt.legend()
    plt.savefig('CNCC/CNCC_Validation_Loss.png')
    plt.show()


history1 = load_json('CNCC/DenseNet121/DenseNet121_epochs50_unfreeze10_history.json')
history2 = load_json('CNCC/DenseNet169/DenseNet169_epochs50_unfreeze20_history.json')
history3 = load_json('CNCC/DenseNet201/DenseNet201_epochs50_unfreeze15_history.json')
history4 = load_json('CNCC/InceptionResNetV2/InceptionResNetV2_epochs50_unfreeze10_history.json')
history5 = load_json('CNCC/ResNet50/Resnet50_epochs50_history_false_unfreeze10.json')
history6 = load_json('CNCC/VGG16/VGG16_epochs50_unfreeze20_history.json')
history7 = load_json('CNCC/VGG19/VGG19_epochs50_freeze_history.json')

plot_multiple_training_histories([history1, history2, history3, history4, history5, history6, history7])

accuracies = []
models = []
# loading the accuracy of each model
# DenseNet121
classification_rapport_DenseNet121 = load_json("CNCC/DenseNet121/DenseNet121_epochs50_unfreeze15_classification_report.json")
accuracy_DenseNet121 = classification_rapport_DenseNet121['accuracy']
accuracies.append(accuracy_DenseNet121)
models.append("DenseNet121")

# DenseNet169
classification_rapport_DenseNet169 = load_json("CNCC/DenseNet169/DenseNet169_epochs50_unfreeze15_classification_report.json")
accuracy_DenseNet169 = classification_rapport_DenseNet169['accuracy']
accuracies.append(accuracy_DenseNet169)
models.append("DenseNet169")

# DenseNet201
classification_rapport_DenseNet201 = load_json("CNCC/DenseNet201/DenseNet201_epochs50_unfreeze15_classification_report.json")
accuracy_DenseNet201 = classification_rapport_DenseNet201['accuracy']
accuracies.append(accuracy_DenseNet201)
models.append("DenseNet201")

# InceptionResNetV2
classification_rapport_InceptionResNetV2 = load_json("CNCC/InceptionResNetV2/InceptionResNetV2_epochs50_unfreeze10_classification_report.json")
accuracy_InceptionResNetV2 = classification_rapport_InceptionResNetV2['accuracy']
accuracies.append(accuracy_InceptionResNetV2)
models.append("InceptionResNetV2")

# RenNet50
classification_rapport_RenNet50 = load_json("CNCC/ResNet50/ResNet50_epochs50_false_unfreeze10_classification_report.json")
accuracy_RenNet50 = classification_rapport_RenNet50['accuracy']
accuracies.append(accuracy_RenNet50)
models.append("ResNet50")

# VGG16
classification_rapport_VGG16 = load_json("CNCC/VGG16/VGG16_epochs50_unfreeze20_classification_report.json")
accuracy_VGG16 = classification_rapport_VGG16['accuracy']
accuracies.append(accuracy_VGG16)
models.append("VGG16")

# VGG19
classification_rapport_VGG19 = load_json("CNCC/VGG19/VGG19_epochs50_freeze_classification_report.json")
accuracy_VGG19 = classification_rapport_VGG19['accuracy']
accuracies.append(accuracy_VGG19)
models.append("VGG19")

# SVM
classification_rapport_SVM = load_json("CNCC/SVM/Classification_report_CNCC_V1_Normalized.json")
accuracy_SVM = classification_rapport_SVM['accuracy']
accuracies.append(accuracy_SVM)
models.append("SVM")

# List of colors for each bar
colors_bar = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple']
plt.figure(figsize=(18, 6))
plt.bar(models, accuracies, color=colors_bar)
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracies')
plt.ylim(0, 1)  # Set the y-axis limits if desired
plt.legend()
plt.savefig('CNCC/CNCC Accuracies.png')
plt.show()