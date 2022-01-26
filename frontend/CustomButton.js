import React, {Component} from 'react';
import {
    TouchableOpacity,
    Text,
    StyleSheet,
  } from 'react-native';
  //export 문은 JavaScript 모듈에서 함수, 객체, 원시 
  //값을 내보낼 때 사용합니다. 
  //내보낸 값은 다른 프로그램에서 import 문으로 
  //가져가 사용할 수 있습니다.

  export default class CustomButton extends Component{
    constructor(props){
      super(props);
    }
  
    render(){
      return (
        <TouchableOpacity style={styles.button} onPress={() => alert('Welcome in ghibli!')}>
          <Text style={styles.title}>START</Text>
        </TouchableOpacity>
      )
    }
  }
  
  const styles = StyleSheet.create({
    button: {
        marginRight: 40,
        marginLeft: 40,
        marginTop: 10,
        paddingTop: 20,
        paddingBottom: 20,
        backgroundColor: '#68a0cf',
        borderRadius: 10,
        borderWidth: 1,
        borderColor: '#fff',
    },
    title: {
        alignItems: 'center',       //centers the View's children on the y-axis
        justifyContent: 'center',   //centers the View's children on the x-axis
        color: 'white',
    },
  });
