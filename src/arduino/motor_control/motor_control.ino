// UWU-RE 2022

const int stepsPerRevolution = 200;
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

  Serial.begin(9600);
  
}

void loop(){
  
}

void calibrate(char axis){
  
  // Calibrate X-axis
  if(axis == "x"){
    int total_x_steps = 0;
    
    // Start from 0
    x_min_stop = digitalRead(x_min);
    digitalWrite(x_dir, HIGH); //set to clockwise
    while(x_min_stop != True){
      digitalWrite(x_step, HIGH);
      x_min_stop = digitalRead(x_min);
    }
    digitalWrite(x_step, LOW);

    //Count Steps
    x_max_stop = digitalRead(x_max);
    digitalWrite(x_dir, LOW); // set to clockwise
    while (x_max_stop != True){
      digitalWrite(x_step, HIGH);
      total_x_steps = total_x_steps + 1
      x_max_stop = digitalRead(x_max);
    }  
  }
}
