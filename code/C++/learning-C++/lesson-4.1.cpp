#include <iostream>
#include <ostream>
int main () {
  
  int num;
  std::cout << "Введите число: "; 
  std::cin >> num;

  bool is_has_car = true;

  if (num > 3 || is_has_car) {    // || - or
    std::cout << "Yes" << std::endl;      // && - and
    if (num == 5)                         //is_has_car == true/is_has_car
      std::cout << "Yess!" << std::endl;  //is_has_car == false/!is_has_car 
  }
  else if (num == 2)
    std::cout << "else if" << std::endl;
  else
    std::cout << "No" << std::endl;

  return 0;
}
