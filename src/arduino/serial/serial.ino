void setup() {
  Serial.begin(9600);
}
void loop() {
  if(Serial.available() > 0) {
    char data = Serial.read();
    char str[2];
    str[0] = data;
    str[1] = '\0';
    Serial.print(str);
  }
}
