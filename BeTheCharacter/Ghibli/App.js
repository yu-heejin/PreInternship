import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import MainScreen from './MainScreen';
import DetailScreen from './DetailScreen';

const Stack = createStackNavigator();
function App() { 
  return ( 
  <NavigationContainer>
    <Stack.Navigator initialRouteName="MAIN">
      <Stack.Screen name="MAIN" component={MainScreen} options={{ title: 'MainScreen' }}/>
      <Stack.Screen name="DETAIL" component={DetailScreen} options={{ title: 'CameraScreen' }}/>
    </Stack.Navigator> 
  </NavigationContainer> ); 
} 

export default App;