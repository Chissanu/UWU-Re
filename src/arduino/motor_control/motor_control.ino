#include <Stepper.h>

// UWU-RE 2022

// Number of steps per revolution
const int stepsPerRevolution = 200;

// Initiate Stepper
Stepper x_stepper(stepsPerRevolution, 1, 2, 3, 4);
Stepper z_stepper(stepsPerRevolution, 5, 6, 7, 8);

// Initiate End stops
#define xMinPin 9
#define xMaxPin 10
#define zMinPin 11
#define zMaxPin 12

int x_min;
int x_max;
int z_min;
int z_max;

// Initiate Max Coords
int x_max_steps;
int z_max_steps;

// Initiate ratio coordinates
int dis1Ratio = 0;
int dis2Ratio = 0;
int dis3Ratio = 0;
int dis4Ratio = 0;
int dis5Ratio = 0;
int dis6Ratio = 0;

// Initiate Current Coordinate
int currentX = 0;

void setup(){
  // set serial port to 9600
  Serial.begin(9600);
  Serial.println("ready");

  // set speed of stepper motor
  x_stepper.setSpeed(100);
  z_stepper.setSpeed(100);

  // set mode of endstop
  pinMode(xMinPin, INPUT);
  pinMode(xMaxPin, INPUT);
  pinMode(zMinPin, INPUT);
  pinMode(zMaxPin, INPUT);
}

void loop(){
  while (Serial.available()){
    String input = Serial.readString();
    input.trim();
    if (input.substring(0, 1) == "c"){
      Serial.println("Calibrating...");
      x_max_steps = calibrate("x", x_stepper, z_stepper);
      z_max_steps = calibrate("z", x_stepper, z_stepper);
      // initiate the coordinates of dispenser
      dispenser1 = x_max_steps * dis1Ratio
      dispenser2 = x_max_steps * dis2Ratio
      dispenser3 = x_max_steps * dis3Ratio
      dispenser4 = x_max_steps * dis4Ratio
      dispenser5 = x_max_steps * dis5Ratio
      dispenser6 = x_max_steps * dis6Ratio
    }
  }
}

int calibrate(String axis, Stepper x_stepper, Stepper z_stepper){
  // calibrate both sides
  int xMaxSteps = 0;
  int zMaxSteps = 0;
  
  if (axis == "x"){
        Serial.println("Calibrating X Axis");
    // x - axis
    x_min = digitalRead(xMinPin);
    while (x_min != 0){
      x_stepper.step(1); // go left until the endstop is pressed
      x_min = digitalRead(xMinPin);
    }
    x_stepper.step(0);
    delay(5000);
    x_max = digitalRead(xMaxPin);
    while (x_max != 0){
      x_stepper.step(-1);
      xMaxSteps += 1;
      x_max = digitalRead(xMaxPin);
    }
    x_stepper.step(0);
    delay(5000);
    z_stepper.step(xMaxSteps); // to not push button
    Serial.println("X calibration complete");
    Serial.println(xMaxSteps);
    return xMaxSteps;
    
  } else if (axis = "z"){
    Serial.println("Calibrating Z Axis");
    // z - axis
    z_min = digitalRead(zMinPin);
    while (z_min != 0){
      z_stepper.step(1); // go left until the endstop is pressed
      z_min = digitalRead(zMinPin);
    }
    z_stepper.step(0);
    delay(5000);
    z_max = digitalRead(zMaxPin);
    while (z_max != 0){
      z_stepper.step(-1);
      zMaxSteps += 1;
      z_max = digitalRead(zMaxPin);
    }
    z_stepper.step(0);
    delay(5000);
    z_stepper.step(zMaxSteps); // to not push button
    Serial.println("Z calibration complete");
    Serial.println(zMaxSteps);
    return zMaxSteps;
  }
}

void dispense(int currentCoords, int dispenserCoords, int xMaxStep, Stepper x_stepper, Stepper z_stepper){
  int distanceLeft = currentCoords - dispenserCoords;
  x_stepper.step(distanceLeft);
  while (z_max != 0){
    
  }
  currentCoords = dispenserCoords;
  
  
 }
