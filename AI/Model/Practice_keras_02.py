# freeze.py
from tensorflow import keras
from torch import pixel_shuffle
import torch
import torch.nn as nn

pixel_shuffle = nn.PixelShuffle(3)
input = torch.randn(1, 9, 4, 4)
output = pixel_shuffle(input)
print(output.size())
torch.Size([1, 1, 12, 12])

model = keras.models.load_model(r'C:\Users\82102\Desktop\faceswap_project2\MOdel\original.h5'
,custom_objects={'PixelShuffler':pixel_shuffle}, compile=False)

export_path = r'C:\Users\82102\Desktop\faceswap_project2\MOdel'
model.save(export_path, save_format="tf")
