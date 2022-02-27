import io                                                         # 파일 경로 접근시 필요한 python 내장 라이브러리
from PIL import Image                                            # Python Imaging Library. 파이썬 인터프리터에 다양한 이미지 파일 형식을 지원,
                
                                                                # 강력한 이미지처리와 그래픽 기능 제공 오픈소스 라이브러리
import numpy as np
from flask import Flask                                            # python web framework 
from flask import request                                        # 웹 요청 관련 모듈
from flask import render_template, redirect, url_for, request    # flask에서 필요한 모듈
from flask import jsonify                                        # import JSON을 해도되지만 여기서는 flask 내부에서 지원하는 jsonify를 사용
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import Sequence                                # 이 모듈이 없으면 사용자가 만든 generator에서 'shape'가 없다고 하는 에러가 발생할 수 있음
import matplotlib.pyplot as plt





app = Flask(__name__)

@app.route("/exam") # 접속 ip혹은 도메인 뒤 붙는 라우터 이름
def predict():
    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory(r"C:\Users\82102\Desktop\faceswap_project2\MOdel",target_size=(100,100), batch_size=100, class_mode='categorical')
    new_model = keras.models.load_model('original.h5')
    new_model.summary()
    loss, acc = new_model.evaluate_generator(test_generator, steps=5) 
    data = {"success": False} # dictionary 형태의 데이터를 만들어 놓고 (딕셔너리에 데이터 넣는 방법1 : dictionary_name = {key:value}) 
    
    data["loss_accuracy"] = acc # 호출한 모델의 정확도를 넣습니다. (딕셔너리에 데이터 넣는 방법2 : dictionary_name[key] = value)
 
    data["success"] = True # 같은 방식으로 가지고 있는 key의 value를 바꿀수 있습니다.
            
    return jsonify(str(acc)) # '/exam'으로 요청을 보낸곳으로 값을 반환하는데에 json형태로 만들어 보내는데 jsonify를 하려면 데이터가 str 형태여야 합니다.

if __name__ == "__main__": # terminal에서 python 인터프리터로 .py 파일을 실행하면 무조건 이 부분을 찾아 실행합니다.
                           # C의 main
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))

    app.run(host="0.0.0.0") # app.run을 해줘야 flask 서버가 구동됩니다. 
                            # host="0.0.0.0"은 외부에서 해당 서버 ip 주소 접근이 가능하도록 하는 옵션입니다.