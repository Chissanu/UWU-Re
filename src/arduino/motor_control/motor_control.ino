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
      calibrate(input.substring(1), , x_stepper, z_stepper);
    }
  }
}

void calibrate(String axis, Stepper x_stepper, Stepper z_stepper){
  // calibrate both sides
  if (axis == "1"){
    Serial.println("Calibrating Both Axis");

    // x - axis
    while (digitalRead())
    x_stepper.step(1); // set direction
    
  }
}
