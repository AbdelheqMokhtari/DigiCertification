# Load your saved model
import h5py
from tensorflow import keras
# List of class names
class_names = ['Avoine', 'Ble dur', 'ble tendre', 'orge', 'triticale']

# Save class names as attributes of the HDF5 file
with h5py.File('Model/CNCC/efficentNet/efficentNet_epochs50_unfreeze5_model.h5', 'a') as file:
    file.attrs['class_names'] = class_names

