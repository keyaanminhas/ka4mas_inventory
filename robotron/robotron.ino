int sen[5];
int s1 = 14;
int s2 = 27;
int s3 = 26;
int s4 = 25;
int s5 = 33;

void sensor_values(){
  sen[0] = digitalRead(s1);
  sen[1] = digitalRead(s2);
  sen[2] = digitalRead(s3);
  sen[3] = digitalRead(s4);
  sen[4] = digitalRead(s5);

}


void setup() {
  pinMode(s1, INPUT);
  pinMode(s2, INPUT);
  pinMode(s3, INPUT);
  pinMode(s4, INPUT);
  pinMode(s5, INPUT);
  Serial.begin(9600);
  Serial.print("STARTING.....");
  
}

void loop() {
  delay(1000);
  sensor_values();
    for (uint8_t i = 0; i < 5; i++)
  {
    Serial.print(sen[i]);}
   Serial.println();
}
