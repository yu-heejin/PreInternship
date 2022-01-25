
import React from 'react';
import {View, ImageBackground, StyleSheet} from 'react-native';
import {Dimensions} from 'react-native';
import CustomButton from './CustomButton';
// 외부에서 패키지를 가져옴

const App = () => {     //실행함수 const 함수이름 
  var {height, width} = Dimensions.get('window');
 
  return (
    <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
      <ImageBackground 
        source={require('./backmain.png')} 
        style={{width:width,height: '100%'}}
        >
        <CustomButton></CustomButton>
      </ImageBackground>
      
  </View>
  )
}

//CSS부분
const styles = StyleSheet.create({
  container: {
    flex : 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;    //메인 액티비티로 내보냄
