void setup() {
  // put your setup code here, to run once:
pinMode(13,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
bool allume;

delay(100);
// Serial.print("A_to_PC");

// String data{""};
  if (Serial.available() > 0) {
      char data;
        data = (char)Serial.read();

    switch (data){
      case '1':
        allume = true;
        break;
      case '0':
        allume = false;
        break;
      default:
        Serial.print("non-ok");
        break;
     }
  if(allume){
    digitalWrite(13,HIGH);
    Serial.print("allume");
    }else{
    digitalWrite(13,LOW);
    Serial.print("eteint");
    }
  
  }


}

