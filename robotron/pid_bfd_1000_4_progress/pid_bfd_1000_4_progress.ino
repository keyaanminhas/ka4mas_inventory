
//********** MOTORS **********//
#define m1 7  //Right Motor MA1
#define m2 8  //Right Motor MA2
#define m3 12  //Left Motor MB1
#define m4 13  //Left Motor MB2
#define e1 5  //Right Motor Enable Pin EA
#define e2 6 //Left Motor Enable Pin EB




//********** EXTRAS **********//
const int b = 0;
const int w = 1;
int pos = 0;
const int sleep = 178;
const int turn_percentage = 97;


//********** PID **********//speed 120  
const double KP = 0.077; //0.07 //0.09 //0.0678 //last working was 0.05  //best 0.05
const double KD = 0.17; //0.1  //0.12  //0.95  //                 0.06  //0.085
const double KI = 0.00000;              //0.0008
double LastError = 0.0;
const int Goal = 2000;
int max_speed = 110;
int I = 0;



//**********5 Channel IR Sensor Connection**********//
int ir0 = 4;
#define ir1 A0
#define ir2 A1
#define ir3 A2
#define ir4 A3
#define ir5 A4
int ir6 = 3;




//*************************************************//


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

void wait_for_white(){
    while ((digitalRead(ir1) == w) && (digitalRead(ir2) == w) && (digitalRead(ir3) == w) && (digitalRead(ir4) == w) && (digitalRead(ir5) == w)){
    delay(10);}
}

void fwd(){
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  digitalWrite(m3, HIGH);
  digitalWrite(m4, LOW);
}



int readline(int s1, int s2, int s3, int s4, int s5){  //if only middle sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == b) && (s4 == w) && (s5 == w))
  {
    pos = 2000;
  }

  if((s1 == w) && (s2 == b) && (s3 == b) && (s4 == b) && (s5 == b))
  {
    pos = 4000;
  }

    if((s1 == w) && (s2 == b) && (s3 == w) && (s4 == b) && (s5 == b))
  {
    pos = 4000;
  }

    if((s1 == b) && (s2 == b) && (s3 == b) && (s4 == b) && (s5 == w))
  {
    pos = 0;
  }
    if((s1 == b) && (s2 == b) && (s3 == w) && (s4 == b) && (s5 == w))
  {
    pos = 0;
  }
  
  
  //if only left sensor detects black line
  if((s1 == b) && (s2 == w) && (s3 == w) && (s4 == w) && (s5 == w))
  {
    pos = 0;
  }
  
  //if only left most sensor detects black line
  if((s1 == b) && (s2 == b) && (s3 == w) && (s4 == w) && (s5 == w))
  {
    pos = 500;
  }

  //if only right sensor detects black line
  if((s1 == w) && (s2 == b) && (s3 == w) && (s4 == w) && (s5 == w))
  {
    pos = 1000;
  }

  //if only right most sensor detects black line
  if((s1 == w) && (s2 == b) && (s3 == b) && (s4 == w) && (s5 == w))
  {
    pos = 1500;
  }

  //if middle and right sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == w) && (s4 == w) && (s5 == b))
  {
    pos = 4000;
  }

  //if middle and left sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == w) && (s4 == b) && (s5 == b))
  {
    pos = 3500;
  }

  //if middle, left and left most sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == w) && (s4 == b) && (s5 == w))
  {
    pos = 3000;
  }

  //if middle, right and right most sensor detects black line
  if((s1 == w) && (s2 == w) && (s3 == b) && (s4 == b) && (s5 == w))
  {
    pos = 2500;
  }
    if((s1 == w) && (s2 == b) && (s3 == b) && (s4 == b) && (s5 == w))
  {
    pos = 2000;
  }
  
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
  pinMode(ir1, INPUT);
  pinMode(ir2, INPUT);
  pinMode(ir3, INPUT);
  pinMode(ir4, INPUT);
  pinMode(ir5, INPUT);
  analogWrite(e1, 0); //you can adjust the speed of the motors from 0-255
  analogWrite(e2, 0); //you can adjust the speed of the motors from 0-255
  fwd();
}
void loop() {
  

    //Reading Sensor Values
  int s0 = digitalRead(ir0);
  int s1 = digitalRead(ir1);  //Left Most Sensor
  int s2 = digitalRead(ir2);  //Left Sensor
  int s3 = digitalRead(ir3);  //Middle Sensor
  int s4 = digitalRead(ir4);  //Right Sensor
  int s5 = digitalRead(ir5);  //Right Most Sensor
  int s6 = digitalRead(ir6);

  

  

  int pos = readline(s1,s2,s3,s4,s5);
  int error = Goal - pos;
  I = I + error;

  int PID = (KP*error) + (KD*(error-LastError)) + (KI * I);

  LastError = error;
  Serial.print(max_speed + PID);
  Serial.print(max_speed - PID);
  Serial.print("\n");

  if (s0 ==0 && s6 == 0){
    
    fwd();
  analogWrite(e1, constrain(max_speed + PID, 0, max_speed)); //you can adjust the speed of the motors from 0-255
  analogWrite(e2, constrain(max_speed - PID, 0, max_speed)); //you can adjust the speed of the motors from 0-255
  }
  else if (s0 == 1){
    delay(sleep);
     analogWrite(e1, max_speed- turn_percentage/100); //you can adjust the speed of the motors from 0-255
     analogWrite(e2, max_speed- turn_percentage/100); //you can adjust the speed of the motors from 0-255
    lleft();
    while (true){
      if (digitalRead(ir0) == 1){
        break;
      }
    }
        while (true){
      if (digitalRead(ir0) == 0){
        break;
      }
    }

  }
    else if (s6 == 1){
      delay(sleep);
     analogWrite(e1, max_speed- turn_percentage/100); //you can adjust the speed of the motors from 0-255
     analogWrite(e2, max_speed- turn_percentage/100); //you can adjust the speed of the motors from 0-255
    rright();
    while (true){
      if (digitalRead(ir6) == 1){
        break;
      }
    }
        while (true){
      if (digitalRead(ir6) == 0){
        break;
      }
    }

  }


  

  
  
}
