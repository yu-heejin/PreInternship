import React from 'react';
import {Text, View, ImageBackground, StyleSheet, TouchableOpacity,} from 'react-native';
import {Dimensions} from 'react-native';

const App = () => {
  var {height, width} = Dimensions.get('window');
 
  return (
    <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
      <ImageBackground 
        source={require('./backmain.png')} 
        style={{width:width,height: '100%'}}
        >
        <TouchableOpacity style={styles.button} onPress={() => alert("지브리!")}>
          <Text style={{
            color: 'white',
            fontFamily: 'GmarketSansTTFMedium',
            fontSize: 25,
            marginTop: 550,
            marginLeft: 175,
          }}>Start</Text>
        </TouchableOpacity>
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