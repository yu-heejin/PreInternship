import React, {Component} from 'react';
import {Text, View, ImageBackground, StyleSheet, TouchableOpacity,} from 'react-native';
import {Dimensions} from 'react-native';

var {height, width} = Dimensions.get('window');

export default class MainScreen extends Component { 
    render() { 
        return ( 
            <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
            <ImageBackground 
              source={require('./backmain.png')} 
              style={{width:width,height: '100%'}}
              >
              <TouchableOpacity style={styles.button} onPress={() => this.props.navigation.push('DETAIL')}>
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
    } goMainScreen(){ 
        this.props.navigation.navigate('DETAIL'); 
    } 
}
const styles = StyleSheet.create({
    container: {
      flex : 1,
      justifyContent: 'center',
      alignItems: 'center',
    },
  });
  