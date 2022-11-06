import { StatusBar } from 'expo-status-bar';
import { Button, SafeAreaView, StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.UwU}>
        UwU:
        <Text style={styles.Re}>Re</Text>
      </Text>
      <Button style = {styles.browseBtn} title="Browse" onPress={() => console.log("Button 1 is pressed")}></Button>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#859FFD',
    alignItems: 'center',
  },
  UwU: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 100,
    fontFamily: 'inter',
    position: 'absolute',
    top:'15%',
  },
  Re: {
    color: 'black',
    fontWeight: 'bold',
    fontSize: 100,
    fontFamily: 'inter',
    top: '0%',
  },
  lineStyle:{
    borderWidth: 0.5,
    borderColor:'black',
    margin:100,
  },
  browseBtn: {
    backgroundColor:'green',
    width: 200,
    height: 800,
  }
});
