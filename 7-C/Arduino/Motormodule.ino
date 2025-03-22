#include <Servo.h>

//Direita e Esquerda
Servo servo_0;
Servo servo_1;
Servo servo_2;
Servo servo_3;

//Cima e Baixo
Servo servo_4;
Servo servo_5;
Servo servo_6;
Servo servo_7;


//Direita e Esquerda
int pot_0 = A0;

//Cima e Baixo
int pot_1 = A1;

//Direita e Esquerda
int val_0;

//Cima e Baixo
int val_1;


void setup()
{
  servo_0.attach(11); //Direita e Esquerda
  servo_1.attach(10);
  servo_2.attach(9); 
  servo_3.attach(8);
  
  servo_4.attach(3);//Cima e Baixo
  servo_5.attach(4);
  servo_6.attach(5);
  servo_7.attach(6);
}

void loop()
{
  val_0 = analogRead(pot_0);
  val_1 = analogRead(pot_1);
  
  
  val_0 = map(val_0, 0, 1023, 0, 180);
  servo_0.write(val_0);
  servo_1.write(val_0);
  servo_6.write(val_0);
  servo_7.write(val_0);
  
  delay(1000);
  
  val_1 = map(val_1, 0, 1023, 0, 180);
  
  servo_2.write(val_1);
  servo_3.write(val_1);
  servo_4.write(val_1);
  servo_5.write(val_1);
  
  delay(1000);
}