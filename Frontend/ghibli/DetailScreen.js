import React, {useState, useRef} from 'react';
import {ImageBackground, TouchableOpacity, View} from 'react-native';
import {RNCamera} from 'react-native-camera';
import {Dimensions, Image} from 'react-native';
import { useColorScheme } from 'react-native';
import CameraRoll from "@react-native-community/cameraroll";

var {height, width} = Dimensions.get('window');


const ProductScanRNCamera = () => {
  const cameraRef = React.useRef(null);
  const [box, setBox] = useState(null);
  const handlerFace = ({faces}) => {
    //console.log(faces);
    if(faces[0]) {
     // console.log(faces);
      setBox({
        boxs: {
          width: faces[0].bounds.size.width,
          height: faces[0].bounds.size.height,
          x: faces[0].bounds.origin.x,
          y: faces[0].bounds.origin.y,
          yawAngle: faces[0].yawAngle,
          rollAngle: faces[0].rollAngle,
        },
        rightEyePosition: faces[0].rightEyePosition,
        leftEyePosition: faces[0].leftEyePosition,
        bottomMouthPosition: faces[0].bottomMouthPosition,
      });
    } else {
      setBox(null);
    }
  }

  const getPhotos = async () => {
      const {edges} = await CameraRoll.getPhotos({
        first: 10,
      });
      console.log('photos', edges[0].node.image);

      const u = edges[0].node.image.uri;
      const formData = new FormData();
      formData.append('imgUrl', {
        uri: Platform.OS === 'android' ? u: u.replace('file://', ''),
        name: 'pic.jpg',
        type: 'image/jpeg',
      })

      fetch(`http://52.78.174.78:8000/jdb`,
      {
          method: 'POST',
          body: formData,
          headers: {
              'Content-Type': 'multipart/form-data'
          }
      }).then(response => response.json())
      .catch(error => console.error('Error:', error));
      
  };
  
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

        getPhotos();
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
              captureAudio={false}
              onFacesDetected={handlerFace}
              faceDetectionLandmarks={RNCamera.Constants.FaceDetection.Landmarks.all} />
               {box && (
              <><Image 
              source = {require('./fff.png')}
            style={styles.totoro({
              rightEyePosition: box.rightEyePosition,
              leftEyePosition: box.leftEyePosition,
              bottomMouthPosition: box.bottomMouthPosition,
              yawAngle: box.yawAngle,
              rollAngle: box.rollAngle,
            })}
              />
                <View
                style= {styles.bound ({
                  width: box.boxs.width,
                  height: box.boxs.height,
                  x: box.boxs.x,
                  y: box.boxs.y,
                })}>

                </View>
              </>
            )}
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
  },
  bound: ({width, height, x, y}) => {
    return {
      position: 'absolute',
      top: y,
      left: x,
      height,
      width,
      borderWidth: 5,
      borderColor: 'red',
      zIndex: 3000,
    };
  },
  totoro: ({rightEyePosition, leftEyePosition, x, y}) => {
    return {
      position: 'absolute',
      top: rightEyePosition.y - 430,
      left: rightEyePosition.x - 100,
      resizeMode: 'contain',
      width: Math.abs(leftEyePosition.x - rightEyePosition.x) + 200,
    }
  }
}; 

export default ProductScanRNCamera;