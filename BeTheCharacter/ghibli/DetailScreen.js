import React, {Component} from 'react';
import {Button, Text, ImageBackground, TouchableOpacity, View} from 'react-native';
import {RNCamera} from 'react-native-camera';
import {Dimensions} from 'react-native';
import { useColorScheme } from 'react-native';

var {height, width} = Dimensions.get('window');

const ProductScanRNCamera = () => {
  const cameraRef = React.useRef(null);

  const takePicture = async () => {
    console.log('cameraRef', cameraRef);
    if (cameraRef) {
      const data = await cameraRef.current.takePictureAsync({
          quality: 1,
          exif: true,
      });
      console.log('찍었지롱');
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
