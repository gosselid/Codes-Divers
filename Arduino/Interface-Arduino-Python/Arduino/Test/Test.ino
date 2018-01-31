

void setup() {
  // put your setup code here, to run once:
pinMode(13,OUTPUT);
pinMode(10,OUTPUT);
Serial.begin(9600);
}

void loop() {
String data;
delay(100);
// Serial.print("A_to_PC");

// String data{""};
  if (Serial.available() > 0) {
bool allume = false;
bool pince = false;
      while(Serial.available()>0)
      {
        data += (char)Serial.read();
      }

  if(data[0]=='A'){
    switch (data[1]){
      case '1':
        allume = true;
        break;
      case '0':
        allume = false;
        break;
      default:
        break;
     }
  }else if(data[0]=='P'){
    switch (data[1]){
      case '1':
        pince = true;
        break;
      case '0':
        pince = false;
        break;
      default:
        break;
     }
  }
      
  
  if(allume){
    digitalWrite(13,HIGH);
        Serial.print("Allume!");
    }else{
    digitalWrite(13,LOW);
        Serial.print("Etteint");
  }
    
  if(pince){
    digitalWrite(10,HIGH);
    Serial.print("P____ON");
    }else{
    digitalWrite(10,LOW);
    Serial.print("P___OFF");
  }
  
  }


}

