import React from 'react' //to create a state
import { Image } from 'expo-image'; //import from react native
import { StatusBar } from 'expo-status-bar'; //import from react native
import { StyleSheet, Text, TextInput, View, Button } from 'react-native'; //dito lahat ng pwedeng components na ilagay

export default function App() {

  const [outputValue, setOutputValue] = React.useState('---'); //anytime you type something, ayun yung gagawin ng setOutput //INITIALIZATION
  const [inputValue, setInputValue] = React.useState('Input value here..'); //INITIALIZATION

function convertToBearing(azimuth) {
    /*
    Compute for the bearing of a given angle.

    Input:
    azimuth - string

    Output:
    bearing - string
    */

    var elements = value.split("-")
    var azimuth = parseFloat(elements[0]) + parseFloat(elements[1])/60 + parseFloat(elements [2])/3600
    setOutputValue(azimuth)// azimuth angle to be split and turned to dd

    if (azimuth > 0 && azimuth < 90) { 
        bearing = 'S '.concat(azimuth.toPrecision(5).toString(), ' W')
    }   else if (azimuth > 90 && azimuth < 180) {
        bearing = 'N '.concat((180-azimuth).toPrecision(5).toString(), ' W')
    }   else if (azimuth > 180 && azimuth < 270) {
        bearing = 'N '.concat((azimuth-180).toPrecision(5).toString(), ' E')
    }   else if (azimuth > 270 && azimuth < 360) {
        bearing = 'S '.concat((360-azimuth).toPrecision(5).toString(), ' E')
    }   else if (azimuth == 0) {
        bearing = 'DUE SOUTH'
    }   else if (azimuth == 90) {
        bearing = 'DUE WEST'
    }   else if (azimuth == 180) {
        bearing = 'DUE NORTH'
    }   else if (azimuth == 270) {
        bearing = 'DUE EAST'
    }   else {
        print()
    }

    var bearing = degrees.toString().concat("-", minutes.toString(), "-", seconds.toString())

    return bearing
}


  //SEPARATE INTO BOXES AND COMPILE THE INITIALIZED VALUES
  return (
    <View style={styles.box}>
      <View style={styles.box1}>
        <Text style={styles.titleText}> AZIMUTH TO BEARING APPLICATION </Text>
      </View>
      
      <View style={styles.box2}> 
        <View style={styles.box21}>
          <Text>Convert your Azimuth to Bearing:</Text>
        </View>
      
    <View style={styles.box3}>
          <TextInput
            style={styles.input}
            onChangeText={setInputValue}
            value={inputValue}
          />
          <Button
            title="Convert"
            onPress={() => convertToBearing(inputValue)}
          />
        </View>  
      </View>

      <View style={styles.box4}>
        <Text style={styles.titleText}> Output: </Text>
        <Text style={styles.titleText}> {outputValue} </Text>
      </View>
    </View> 
  );
}

//INITIALIZATION
//DEFINING VALUES
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  box1: {
    width: '100%', 
    height: '10%', 
    alignItems: 'center', 
    justifyContent: 'center'        
  },
  box2: {
    width: '100%', 
    height: '25%', 
    alignItems: 'center', 
    justifyContent: 'center',      
    padding: 10  
  },
  box21: {
    width: '100%', 
    height: '10', 
  },
  box3: {
    flex: 1,
    width: '100%',
    height: '25%',
    alignItems: 'center', 
    justifyContent: 'center',      
    padding: 10 
  },
  box4: {
    width: '100%', 
    height: '50%', 
    alignItems: 'center', 
    justifyContent: 'center'           
  },
  titleText: {
    fontSize: 24,
    fontWeight: 'bold', 
    color: 'black'
  },
  image: {
    flex: 1,
    width: '100%',
    backgroundColor: '#0553',
  },
  input: {
    height: '50%',
    width: '70%',
    fontSize: 24,
    color: 'black'
  }
});

/*
The react native components much needed in this design are text, textinput, button, view, and stylesheet, and the code above is how I will implement it. It will appear as a direct converter in which all the users will
have to do are to input their designated azimuth and press the convert button for the output(bearing) to appear. The sizes will be adjusted for the general overview of the app and the view feature (containers) will be split 
into 4 (1 shall be inside another so the total boxes created were 5). The much needed textinput wil indicate the box for the users to type their azimuth values in. The text feature will help guide the users on what to
do and provide the output as well. Lastly, the button will be the main catalyst to convert the submitted values in the textinput for it to appear in the text output.

*/