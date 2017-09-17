#include <VarSpeedServo.h>


const byte numChars = 32;
char receivedChars[numChars];

boolean newData = false;

VarSpeedServo servo1; VarSpeedServo servo2;
String inputString = "";         // a string to hold incoming data



void setup() 
{
  servo1.attach(14);
  servo2.attach(10);

  Serial.begin(9600);
  Serial.println("Ready");


}


void loop() 
{
    receiveSerial();
    updateServo(); 
}


void receiveSerial() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void updateServo() {
    
    signed int vel, dir;
    unsigned int pos;
    char comand;

//    protocolo utilizado é: [comando][valor]
    if (newData == true) 
    {
      newData = false;
      vel = receivedChars[2];
      dir = receivedChars[1];
      comand = receivedChars[0];
      Serial.println(receivedChars[0]);
      Serial.println(receivedChars[1]);
      


      
//      Serial.print (receivedChars);
      
      if (comand == 'x')
      {  
        if (vel > 2 && not dir)
        {
          servo1.write(180, vel, false);    
        }
        else if (vel > 2 && dir)
        {
          servo1.write(0, vel, false);    
        }
        else
        {
          pos = servo1.read();
          servo1.write(pos, 255, false);       
        }
      }
      if (comand == 'y')
      {
        if (vel > 2)
        {
          servo2.write(180, vel, false);    
        }
        else if (vel < -2)
        {
          servo2.write(0, -vel, false);    
        }
        else
        {
          pos = servo1.read();
          servo2.write(pos, 255, false);       
        }
      }     

        
    }
}

