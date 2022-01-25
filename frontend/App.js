import React from 'react';
import {Text, View, Button, Image, ImageBackground, StyleSheet} from 'react-native';
import {Dimensions, Toolbar} from 'react-native';

const App = () => {
  var {height, width} = Dimensions.get('window');
  return (
    <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
      <ImageBackground 
        source={require('./img/backmain.png')} 
        style={{width:width,height: '100%'}}
        >
        <Button
        title="Press me"
        onPress={() => alert('Simple Button pressed')}
        />
      </ImageBackground>
      
  </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex : 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
