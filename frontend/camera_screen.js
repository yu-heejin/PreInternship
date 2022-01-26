import React from 'react';
import {Text, View, StyleSheet} from 'react-native';

const subScreen = () => {
  return (
    <View style={{flex:1,backgroundColor: '#246dd5', alignItems: 'center'}}>
        <Text>There will be Camera Function.</Text>
        <TouchableOpacity style={styles.button} onPress={() => navigation.navigate("App")}>
          <Text style={{
            fontFamily: Fonts.GmarketSansTTFMedium,
            fontSize: 25,
            marginTop: 330,
            marginLeft: 175,
          }}>Back to main</Text>
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

export default subScreen;
