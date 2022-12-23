#define m1 7  //Right Motor MA1
#define m2 8  //Right Motor MA2
#define m3 12  //Left Motor MB1
#define m4 13  //Left Motor MB2
#define e1 5  //Right Motor Enable Pin EA
#define e2 6 //Left Motor Enable Pin EB
#define bspeed 250
int b = 0;
int w = 1;
int error = 0;
int ini = 125;
int Kp = 50;

//**********5 Channel IR Sensor Connection**********//
#define ir1 A0
#define ir2 A1
#define ir3 A2
#define ir4 A3
#define ir5 A4
//*************************************************//

void setup() {
  Serial.begin(9600);
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
  analogWrite(e1, bspeed); //you can adjust the speed of the motors from 0-255
  analogWrite(e2, bspeed); //you can adjust the speed of the motors from 0-255
  fwd();
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

  int error_code = get_error(s1,s2,s3,s4,s5);
  Serial.print(s1);
  Serial.print(s2);
  Serial.print(s3);
  Serial.print(s4);
  Serial.print(s5);
  Serial.print("\n");
  Serial.print(error_code);
  Serial.print("\n");



  //PID

  int speed1 =  0 + ini - (error_code*Kp);
  int speed2 =  250 - ( ini - error_code*Kp);
  Serial.print(speed1);
  Serial.print("     ");
  Serial.print(speed2);
  Serial.print("\n\n");
  analogWrite(e1,speed1);
  analogWrite(e2, speed2);
  
  }



int get_error(int s1, int s2, int s3, int s4, int s5){  //if only middle sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == b) && (s4 == w) && (s5 == w))
  {
    error = 0;
  }
  
  //if only left sensor detects black line
  if((s1 == b) && (s2 == w) && (s3 == w) && (s4 == w) && (s5 == w))
  {
    error = -4;
  }
  
  //if only left most sensor detects black line
  if((s1 == b) && (s2 == b) && (s3 == w) && (s4 == w) && (s5 == w))
  {
    error = -3;
  }

  //if only right sensor detects black line
  if((s1 == w) && (s2 == b) && (s3 == w) && (s4 == w) && (s5 == w))
  {
    error = -2;
  }

  //if only right most sensor detects black line
  if((s1 == w) && (s2 == b) && (s3 == b) && (s4 == w) && (s5 == w))
  {
    error = -1;
  }

  //if middle and right sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == w) && (s4 == w) && (s5 == b))
  {
    error = 4;
  }

  //if middle and left sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == w) && (s4 == b) && (s5 == b))
  {
    error = 3;
  }

  //if middle, left and left most sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == w) && (s4 == b) && (s5 == w))
  {
    error = 2;
  }

  //if middle, right and right most sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == b) && (s4 == b) && (s5 == w))
  {
    error = 1;
  }
  return error;
}
