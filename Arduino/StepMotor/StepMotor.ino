double inter_temps=230; //microsecondes

int PinPul = 7;
int PinDir = 6;
int PinEnbl = 5;


void setup() {
  // put your setup code here, to run once:
  pinMode(PinPul,OUTPUT);
  pinMode(PinDir,OUTPUT);
  pinMode(PinEnbl,OUTPUT);
  digitalWrite(PinPul,LOW);
  digitalWrite(PinEnbl,LOW);
  digitalWrite(PinDir,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:


for(long i=1; i<50000; i++){
    digitalWrite(PinPul, HIGH);
    digitalWrite(PinPul, LOW);
   
    delayMicroseconds(inter_temps);
  }

  exit(0);
}
