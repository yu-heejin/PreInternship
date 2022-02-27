# freeze.py
from tensorflow import keras
model = keras.models.load_model(r'C:\Users\82102\Desktop\faceswap_project2\MOdel\original.h5', compile=False)

export_path = 'androidpb'
model.save(export_path, save_format="tf")
