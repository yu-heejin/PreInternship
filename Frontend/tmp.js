import React from 'react';
import {Text, View, ImageBackground, StyleSheet, TouchableOpacity,} from 'react-native';
import {Dimensions} from 'react-native';
import Main from './Main';
import Camera from './Camera';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

const App = () => {
  var {height, width} = Dimensions.get('window');
 
  return (
    <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen name='Main' component={Main}/>
      <Stack.Screen name='Camera' component={Camera}/>
    </Stack.Navigator>
  </NavigationContainer>
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

import React from 'react';
import {Text, View, ImageBackground, StyleSheet, TouchableOpacity,} from 'react-native';
import {Dimensions} from 'react-native';

const Main = () => {
  var {height, width} = Dimensions.get('window');
 
  return (
    <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
      <ImageBackground 
        source={require('./img/backmain.png')} 
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

export default Main;

import React from 'react';
import {Text, View, StyleSheet, TouchableOpacity,} from 'react-native';

const Camera = () => {
  return (
    <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
        <TouchableOpacity style={styles.button} onPress={() => alert("지브리!")}>
          <Text style={{
            color: 'white',
            fontFamily: 'GmarketSansTTFMedium',
            fontSize: 25,
            marginTop: 550,
            marginLeft: 175,
          }}>Under Construction for Camera. Click to Back to the MainActivity.</Text>
        </TouchableOpacity>
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

export default Camera;
