
import React from 'react';
import {Text, View, Button, Image, StyleSheet} from 'react-native';
import {Dimensions, Toolbar} from 'react-native';

const App = () => {
  var {height, width} = Dimensions.get('window');
  return (
    <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
      <Image
        source={require('./img/backmain.png')} 
        style={{width:width,height: '100%'}}
      />
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
