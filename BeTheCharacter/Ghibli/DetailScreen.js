import React, {Component} from 'react';
import {Text, View, ImageBackground, StyleSheet, TouchableOpacity,} from 'react-native';

export default class DetailScreen extends Component {
    render() { 
        return ( 
            <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
            <TouchableOpacity style={styles.button} onPress={() => this.props.navigation.push('MAIN')}>
              <Text style={{
                color: 'white',
                fontFamily: 'GmarketSansTTFMedium',
                fontSize: 25,
                marginTop: 250
              }}>Under Construction for Camera. Click to Back to the mainActivity.</Text>
            </TouchableOpacity>
      </View>
        ); 
    } 
}

const styles = StyleSheet.create({
    container: {
      flex : 1,
      justifyContent: 'center',
      alignItems: 'center',
    },
  });