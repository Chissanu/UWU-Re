#include <Stepper.h>

// UWU-RE 2022

// pin setup
const int x_step = A0;
const int x_dir = A1;
const int z_step = 46;
const int z_dir = 48;
const int x_min = 2;
const int x_max = 3;
const int z_min = 18;
const int z_max = 19;

// end stop
bool x_min_stop = false;
bool x_max_stop = false;
bool z_min_stop = false;
bool z_max_stop = false;

//setup pinmode and stuff
void setup(){
  pinMode(x_step, OUTPUT);
  pinMode(x_dir, OUTPUT);
  pinMode(z_step, OUTPUT);
  pinMode(z_dir, OUTPUT);
  pinMode(x_min, INPUT);
  pinMode(x_max, INPUT);
  pinMode(z_min, INPUT);
  pinMode(z_max, INPUT);
}

void loop(){
  
}

void calibrate(char axis){
  // Calibrate X-axis
  if(axis == "x"){
    // Calibrate Minimum distance
    while(x_min_stop != True){
      digitalWrite()
    }
    
  }
}
