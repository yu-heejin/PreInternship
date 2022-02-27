
import requests 
import base64
from base64 import encodebytes
from PIL import Image
import io
import matplotlib.pyplot as plt

#서버 주소 저장
addr = 'http://localhost:5000'
face_swap_url = addr + '/api/face_swap'


def encode_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img

# send http request with image and receive response
response = requests.post(face_swap_url,  json={'face':encode_image(r'C:\Users\82102\Desktop\faceswap_project2\OutputA\001.jpg'),'body':encode_image(r'C:\Users\82102\Desktop\faceswap_project2\OutputA\00001.jpg')})

#이미지 추출, 베이스64: 64진법 변환
img = response.json()['image']
img = base64.b64decode(img)  
img = Image.open(io.BytesIO(img))
plt.imshow(img)

