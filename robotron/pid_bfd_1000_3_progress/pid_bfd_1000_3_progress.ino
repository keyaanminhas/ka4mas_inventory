
//********** MOTORS **********//
#define m1 7  //Right Motor MA1
#define m2 8  //Right Motor MA2
#define m3 12  //Left Motor MB1
#define m4 13  //Left Motor MB2
#define e1 5  //Right Motor Enable Pin EA
#define e2 6 //Left Motor Enable Pin EB




//********** EXTRAS **********//
int b = 0;
int w = 1;
int pos = 0;


//********** PID **********//speed 120  
const double KP = 0.05; //0.07 //0.09 //0.0678
const double KD = 0.06; //0.1  //0.12  //0.95
const double KI = 0.0000;              //0.0008
double LastError = 0.0;
const int Goal = 3000;
int max_speed = 120;
int I = 0;
int lastpos = 0;



//**********5 Channel IR Sensor Connection**********//
int ir0 = 4;
#define ir1 A0
#define ir2 A1
#define ir3 A2
#define ir4 A3
#define ir5 A4
int ir6 = 3;




//*************************************************//

void wait_for_white(){
//    analogWrite(e1, max_speed); //you can adjust the speed of the motors from 0-255
//    analogWrite(e2, max_speed); //you can adjust the speed of the motors from 0-255
    delay(300);
    while ((digitalRead(ir0) == b) && (digitalRead(ir1) == w) && (digitalRead(ir2) == w) && (digitalRead(ir3) == w) && (digitalRead(ir4) == w) && (digitalRead(ir5) == w) && (digitalRead(ir6) == b)){
    delay(10);}
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

void fwd(){
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  digitalWrite(m3, HIGH);
  digitalWrite(m4, LOW);
}



int readline(int ir0, int ir1, int ir2, int ir3, int ir4, int ir5, int ir6){  //if only middle sensor detects black line
  
  if ((ir0 == 0) && (ir1 == 0) && (ir2 == 0) && (ir3 == 0) && (ir4 == 0) && (ir5 == 0) && (ir6 == 0)){
    return pos;
    }
  pos = ((ir0 * 0) + (ir1 * 1000) + (ir2 * 2000) + (ir3 * 3000) + (ir4 * 4000) + (ir5 * 5000) + (ir6 * 6000))/(ir0 + ir1 + ir2 + ir3 + ir4 + ir5 + ir6);
  
  return pos;
}


void setup() {
  //Serial.begin(9600);
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(m3, OUTPUT);
  pinMode(m4, OUTPUT);
  pinMode(e1, OUTPUT);
  pinMode(e2, OUTPUT);
  pinMode(ir0, INPUT);
  pinMode(ir1, INPUT);
  pinMode(ir2, INPUT);
  pinMode(ir3, INPUT);
  pinMode(ir4, INPUT);
  pinMode(ir5, INPUT);
  pinMode(ir6, INPUT);
  analogWrite(e1, 0); //you can adjust the speed of the motors from 0-255
  analogWrite(e2, 0); //you can adjust the speed of the motors from 0-255
  fwd();
}
void loop() {

  fwd();

    //Reading Sensor Values
  int s0 = digitalRead(ir0);  //Left Most Sensor
  int s1 = !digitalRead(ir1);  //Left Most Sensor
  int s2 = !digitalRead(ir2);  //Left Sensor
  int s3 = !digitalRead(ir3);  //Middle Sensor
  int s4 = !digitalRead(ir4);  //Right Sensor
  int s5 = !digitalRead(ir5);  //Right Most Sensor
  int s6 = digitalRead(ir6);  //Left Most Sensor


  int pos = constrain(readline(s0,s1,s2,s3,s4,s5,s6), 0, 6000);

  if (s0 == 1){
    pos = 0;
    wait_for_white();
    }
  if (s6 == 1){
    pos = 6000;
    wait_for_white();
  }

  
  Serial.print(s0);
  Serial.print(s1);
  Serial.print(s2);
  Serial.print(s3);
  Serial.print(s4);
  Serial.print(s5);
  Serial.print(s6);
  
  Serial.print("\n");
  Serial.print(pos);
  Serial.print("\n\n");

  int error = Goal - pos;
  I = I + error;

  int PID = (KP*error) + (KD*(error-LastError)) + (KI * I);

  LastError = error;
//  Serial.print(max_speed + PID);
//  Serial.print(max_speed - PID);
//  Serial.print("\n");
  
  analogWrite(e1, constrain(max_speed + PID, 0, max_speed)); //you can adjust the speed of the motors from 0-255
  analogWrite(e2, constrain(max_speed - PID, 0, max_speed)); //you can adjust the speed of the motors from 0-255

    if (s0 == 1){
    while (digitalRead(ir0) == 1){
      delay(1);
      analogWrite(e1, max_speed); //you can adjust the speed of the motors from 0-255
      analogWrite(e2, max_speed); //you can adjust the speed of the motors from 0-255
      left();
    }
  }
  if (s6 == 1){
    while (digitalRead(ir6)== 1){
      delay(1);
      analogWrite(e1, max_speed); //you can adjust the speed of the motors from 0-255
      analogWrite(e2, max_speed); //you can adjust the speed of the motors from 0-255
      right();
  }
  
}
}
