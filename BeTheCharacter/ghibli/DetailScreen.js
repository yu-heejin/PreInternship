import React from 'react';
import {Button, Text, ImageBackground, TouchableOpacity, View} from 'react-native';
import {RNCamera} from 'react-native-camera';
import {Dimensions} from 'react-native';
import { useColorScheme } from 'react-native';
import CameraRoll from "@react-native-community/cameraroll";

var {height, width} = Dimensions.get('window');

const ProductScanRNCamera = () => {
  const cameraRef = React.useRef(null);

  const submitData = (UriData, save) => {
    fetch("http://10.0.2.2:3000/send-data", {
      method: "post",
      headers: {
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        picture: UriData,
        result: save
      })
    })
    .then(res.json())
    .then(data => {
      console.log(data)
    })
    .catch(err => {
      console.log(err)
    })
  }

  const takePicture = async () => {
    console.log('cameraRef', cameraRef);
    if (cameraRef) {
      const data = await cameraRef.current.takePictureAsync({
          quality: 1,
          exif: true,
      });
      console.log('data', data.uri);

      if (data) {
        const result = await CameraRoll.save(data.uri);
        console.log('result', result);
        submitData(data.uri, result);
      }
    }
  }
    return (
      <View
        style={{
          flex: 1,
          justifyContent: 'center',
          alignItems: 'center',
          backgroundColor: '#246dd5'
        }}
      ><ImageBackground 
      source={(useColorScheme() == 'light') ? require('./cam1.jpeg') : require('./cam2.jpeg')} 
      style={{width:width,height: '100%',
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#246dd5'}}
      >
            <RNCamera
              ref={cameraRef}
              style={{
                width:300, height:500
              }}
              type={RNCamera.Constants.Type.front}
              captureAudio={false} />
            
              <TouchableOpacity onPress={takePicture}
              style={{marginTop: 30,
                orderWidth:1,
                borderColor:'rgba(0,0,0,0.2)',
                alignItems:'center',
                justifyContent:'center',
                width:80,
                height:80,
                backgroundColor:(useColorScheme() == 'light') ?'#ffd5dc' : '#cdd9ff',
                borderRadius:100,
                borderWidth: 10,
                borderColor: '#fff'}}>
              </TouchableOpacity>
              </ImageBackground>
      </View>

    );
}

const styles = {
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  button: {
    width: 100,
    height: 100,
    borderRadius: 50,
    backgroundColor: 'pink'
  }
};

export default ProductScanRNCamera;

