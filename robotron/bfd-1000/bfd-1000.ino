#define m1 7  //Right Motor MA1
#define m2 8  //Right Motor MA2
#define m3 12  //Left Motor MB1
#define m4 13  //Left Motor MB2
#define e1 5  //Right Motor Enable Pin EA
#define e2 6 //Left Motor Enable Pin EB

int b = 0;
int w = 1;



//**********5 Channel IR Sensor Connection**********//
#define ir1 A0
#define ir2 A1
#define ir3 A2
#define ir4 A3
#define ir5 A4
//*************************************************//

void setup() {
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(m3, OUTPUT);
  pinMode(m4, OUTPUT);
  pinMode(e1, OUTPUT);
  pinMode(e2, OUTPUT);
  pinMode(ir1, INPUT);
  pinMode(ir2, INPUT);
  pinMode(ir3, INPUT);
  pinMode(ir4, INPUT);
  pinMode(ir5, INPUT);
  analogWrite(e1, 255); //you can adjust the speed of the motors from 0-255
  analogWrite(e2, 255); //you can adjust the speed of the motors from 0-255
}


void fwd(){
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  digitalWrite(m3, HIGH);
  digitalWrite(m4, LOW);
}
void right(){
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(m3, HIGH);
  digitalWrite(m4, LOW);
}
void rright(){
  digitalWrite(m1, LOW);
  digitalWrite(m2, HIGH);
  digitalWrite(m3, HIGH);
  digitalWrite(m4, LOW);
}
void left(){
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
}

void lleft(){
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, HIGH);
}
void back(){
  digitalWrite(m1, LOW);
  digitalWrite(m2, HIGH);
  digitalWrite(m3, LOW);
  digitalWrite(m4, HIGH);
}

void stp(){
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
}


void loop() {
  //Reading Sensor Values
  int s1 = digitalRead(ir1);  //Left Most Sensor
  int s2 = digitalRead(ir2);  //Left Sensor
  int s3 = digitalRead(ir3);  //Middle Sensor
  int s4 = digitalRead(ir4);  //Right Sensor
  int s5 = digitalRead(ir5);  //Right Most Sensor


  //if only middle sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == b) && (s4 == w) && (s5 == w))
  {
    fwd();
  }

  
  
  //if only left sensor detects black line
  if((s1 == w) && (s2 == b) && (s3 == w) && (s4 == w) && (s5 == w))
  {
    left();
  }
  
  //if only left most sensor detects black line
  if((s1 == b) && (s2 == w) && (s3 == w) && (s4 == w) && (s5 == w))
  {
    lleft();
  }

  //if only right sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == w) && (s4 == b) && (s5 == w))
  {
    right();
  }

  //if only right most sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == w) && (s4 == w) && (s5 == b))
  {
    rright();
  }

  //if middle and right sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == b) && (s4 == b) && (s5 == w))
  {
    right();
  }

  //if middle and left sensor detects black line
  if((s1 == w) && (s2 == b) && (s3 == b) && (s4 == w) && (s5 == w))
  {
    left();
  }

  //if middle, left and left most sensor detects black line
  if((s1 == b) && (s2 == b) && (s3 == b) && (s4 == w) && (s5 == w))
  {
    //going right with full speed 
    left();
  }

  //if middle, right and right most sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == b) && (s4 == b) && (s5 == b))
  {
    right();
  }

  //if all sensors are on a black line
  if((s1 == b) && (s2 == b) && (s3 == b) && (s4 == b) && (s5 == b))
  {
    stp();
  }
  
  //if all sensors are on a black line
  if((s1 == w) && (s2 == b) && (s3 == b) && (s4 == b) && (s5 == w))
  {
    fwd();
  }
}
