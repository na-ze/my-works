#include <iostream>
#include <iterator>

int main () {
  int num;
  std::cout << "Введите число: ";
  std::cin >> num;

  switch(num){
    case 5:
      std::cout << " Num is 5" << std::endl;
      break;
    case 50:
      std::cout << " Num is 50" << std::endl;
      break;
    case 3:
      std::cout << " Num is 3" << std::endl;
      break;
    case 25:
      std::cout << " Num is 25" << std::endl;
      break;
    default:
      std::cout << "bruh" << std::endl;
      break;
  }

  return 0;
}
