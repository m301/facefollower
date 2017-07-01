#include   <Servo.h>

Servo servoX;
Servo servoY;
int servoDelay =15; //delay to allow the servo to reach position;
 
int pos = 0;    // variable to store the servo position

void setup() {
  servoX.attach(9); 
  servoY.attach(8); 
  Serial.begin(9600);
}

void loop() {
   if (Serial.available()) {
    getInt();
    int x = getInt();
    Serial.println(String(x));
    servoX.write(x);
    servoY.write(getInt());
    delay(servoDelay);
   }
}


int getInt() {
  return getInt(0);
}
int getInt(int sum) {
  // Read a single character from the serial input stream.
  char c;
  
  while((c = Serial.read())!='\0'){
    if (c <'0' ||  c > '9') 
      return sum;
   else
    sum = sum * 10+((int) (c - '0')); 
  }  
  return sum;
}
