# UWU-Re  
UWU-Re is a cocktail machine which mix 6 different drinks. The drink can be ordered using your mobile phones using webapp. This machine is a our year 2 semester 1 project which is made for 2 subjects, CPS (Cyber - Physical System) and PCA (Principal of Computation and Application).
## List Of Materials
The 3d parts are provided in the provided folder. The 3d printer used is creality ender 3 without any upgrades. You can print the component using the printer itself out of the box. The settings for the 3d printer will also be provided in the folder
## The Model
Our machine will be a drink dispenser based on gravity. This means there we won't need any pump to dispense drinks. We will instead use valves to get the amount of liquid needed as seen in the picture

![alt text](https://github.com/Chissanu/UWU-Re/blob/main/pictures/machine_sketch.jpg)

As seen in the picture above, the bottles are installed vertically so that the content inside is at the bottleneck. In addition, the push valve is installed at the tip of the bottle for a precise 5 oz (~ 148 milliliters) and will be pushed by a motor installed on a slider (pink part) in which the slider will also be controlled by a stepper motor at the right side of the machine. Think of this as the machine moving only at the direction x axis and z axis. The blue part is the LCD screen installed for the raspberry pi 4 for Tkinter for user interface. All the electronic component is installed at the side of the machine to prevent damage to the circuitries from leakage. A 3D visualisation can bee seen [here](https://www.tinkercad.com/things/1XuOXg0HMAo?sharecode=GJE946JQ6UPPvVI4ZD06l16DsZAhe3jpPH0mlR12uSo)

### Side view
![alt text](https://github.com/Chissanu/UWU-Re/blob/main/pictures/3d1.png)

### Side view
![alt text](https://github.com/Chissanu/UWU-Re/blob/main/pictures/3d2.png)

### Back view
![alt text](https://github.com/Chissanu/UWU-Re/blob/main/pictures/3d3.png)

## How it works
Our software will have 2 interfaces which is a UI in Tkinter (A python interface) which will be shown on the screen from the machine and a website which the user can order their drinks using their phones. Both of the interface will send input to a python program to fetch the array of recipe from the database stored in a JSON file. After the python program fetch the recipe, the recipe is then sent to Arduiono to dispense the drink

## Colaborators    
Chalatsorn Tantiyamas 64011361  
Chissanu Kittipakorn 64011728  
Phanuruj Sotthidat 64011544  
Siraphop Mukdaphetcharat 64011614  
