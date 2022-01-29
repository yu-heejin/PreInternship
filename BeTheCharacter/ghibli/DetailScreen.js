import React, {Component} from 'react';
import {Button, Text, TouchableOpacity, View} from 'react-native';
import {RNCamera} from 'react-native-camera';

const ProductScanRNCamera = () => {
  const cameraRef = React.useRef(null);

  const takePicture = async () => {
    console.log('cameraRef', cameraRef);
    if (cameraRef) {
      const data = await cameraRef.current.takePictureAsync({
          quality: 1,
          exif: true,
      });
      console.log('data', data);
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
      >
            <RNCamera
              ref={cameraRef}
              style={{
                width:200, height:400
              }}
              type={RNCamera.Constants.Type.front}
              captureAudio={false} />
            
              <TouchableOpacity onPress={takePicture}
              style={{marginTop: 30}}>
                <Button title="Take" style={{
                  width: 100,
                  height: 100,
                  borderRadius: 50,
                  color: '72c0ff'
                }}/>
              </TouchableOpacity>
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

