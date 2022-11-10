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

void setup(){
  // set serial port to 9600
  Serial.begin(9600);
  Serial.println("ready");

  // set speed of stepper motor
  x_stepper.setSpeed(60);
  z_stepper.setSpeed(60);

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
      Serial.println("Calibrate");
      calibrate(input.substring(1), x_stepper, z_stepper);
    }
  }
}

int calibrate(String axis, Stepper x_stepper, Stepper z_stepper){
  // calibrate both sides
  int xMaxSteps = 0;
  int zMaxSteps = 0;
  if (axis == "1"){
    Serial.println("Calibrating Both Axis");

    // x - axis
    x_min = digitalRead(xMinPin);
    while (x_min != 1){
      x_stepper.step(-1); // go left until the endstop is pressed
      x_min = digitalRead(xMinPin);
    }
    x_max = digitalRead(xMaxPin);
    while (x_max != 1){
      x_stepper.step(1);
      xMaxSteps += 1;
    }
    x_stepper.step(xMaxSteps); // to not push button
    
        // z - axis
    z_min = digitalRead(zMinPin);
    while (z_min != 1){
      z_stepper.step(-1); // go left until the endstop is pressed
      z_min = digitalRead(zMinPin);
    }
    z_max = digitalRead(zMaxPin);
    while (z_max != 1){
      z_stepper.step(1);
      zMaxSteps += 1;
    }
    z_stepper.step(zMaxSteps); // to not push button
    
  } else if (axis == "2"){
    Serial.println("Calibrating X Axis");
    
    // x - axis
    x_min = digitalRead(xMinPin);
    while (x_min != 1){
      x_stepper.step(-1); // go left until the endstop is pressed
      x_min = digitalRead(xMinPin);
    }
    x_max = digitalRead(xMaxPin);
    while (x_max != 1){
      x_stepper.step(1);
      xMaxSteps += 1;
    }
    x_stepper.step(-xMaxSteps); // to not push button
    
  } else if (axis = "3"){
    Serial.println("Calibrating Z Axis");
    // z - axis
    z_min = digitalRead(zMinPin);
    while (z_min != 1){
      z_stepper.step(-1); // go left until the endstop is pressed
      z_min = digitalRead(zMinPin);
    }
    z_max = digitalRead(zMaxPin);
    while (z_max != 1){
      z_stepper.step(1);
      zMaxSteps += 1;
    }
    z_stepper.step(-zMaxSteps); // to not push button
  }
}
