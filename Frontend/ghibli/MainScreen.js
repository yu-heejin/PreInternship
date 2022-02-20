import React, {Component} from 'react';
import {Text, View, ImageBackground, StyleSheet, TouchableOpacity, useColorScheme,} from 'react-native';
import {Dimensions} from 'react-native';

var {height, width} = Dimensions.get('window');

const MainScreen = ({ navigation }) => {
        return ( 
            <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
            <ImageBackground 
              source={(useColorScheme() == 'light') ? require('./backmain.png') : require('./backmaind.png')} 
              style={{width:width,height: '100%'}}
              >
              <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('DETAIL')}>
                <Text style={{
                  color: 'white',
                  fontFamily: 'GmarketSansTTFMedium',
                  fontSize: 25,
                  marginTop: 510,
                  marginLeft: 175,
                }}>Start</Text>
              </TouchableOpacity>
            </ImageBackground>
        </View> 
        ); 
}
const styles = StyleSheet.create({
    container: {
      flex : 1,
      justifyContent: 'center',
      alignItems: 'center',
    },
  });

  export default MainScreen;