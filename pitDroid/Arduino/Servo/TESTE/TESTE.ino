#include <VarSpeedServo.h>

VarSpeedServo servo1; VarSpeedServo servo2;
String inputString = "";         // a string to hold incoming data

void setup() {
  servo1.attach(14);
  servo2.attach(10);

  Serial.begin(9600);
  Serial.println("Ready");
}

void loop() 
{

  static int v = 0;


  if (Serial.available()) 
  {
    inputString = Serial.readStringUntil('!');
    Serial.print(inputString + "foi");
    v = inputString.toInt();
    Serial.print(v);
    servo1.write(v);
    inputString = "";
  }

//
//  if ( Serial.available()) {
//    char ch = Serial.read();
//
//    switch (ch) {
//      case '0'...'9':
//        v = v * 10 + ch - '0';
//
//        break;
//      case 's':
//        servo1.write(v);
//        v = 0;
//        break;
//      case 'w':
//        servo2.write(v);
//        v = 0;
//        break;
//      case 'd':
//        servo2.detach();
//        break;
//      case 'a':
//        servo2.attach(10);
//        break;
//    }
//  }
}
