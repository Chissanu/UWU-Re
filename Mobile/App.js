import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.UwU}>
        UwU:
        <Text style={styles.Re}>Re</Text>
      </Text>
      <Text style>Hello</Text>
      <StatusBar style="auto" />
    </View>

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
  }
});
