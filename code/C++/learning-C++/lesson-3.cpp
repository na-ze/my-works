#include <iostream>

int main () {
  //Использование переменных
  int num = -45;
  num = 3;
  std::cout << "Перменная: " << num << std::endl;
  
  int a;
  std::cout << "Введите переменную a:";
  std::cin >> a;
  std::cout << "A:" << a << std::endl;
  //Типы данных(integers)
  short num1 = 7; //2 byte /-32k to 32k
  int num2 = 5;   //4 byte /-2B to 2B
  long num3 =5;   //8 byte /-more to more
  unsigned short b;   //Before any of the above removes -, but adds +
  //Float
  float num4 = 5.839456f;
  double num5 = 453.56789912f;
  //Char
  char sym = '&';
  //Boolean
  bool happy = true;
  return 0;
}
