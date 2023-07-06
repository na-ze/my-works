#include <iostream>

using namespace std;

int main () {
  //for
  for(int i = 100; i >= 10; i-=15)
    std::cout << "1.EL: " << i << std::endl;
  //while
  int j = 0;
  while (j < 10) {
    std::cout << "2.El: " << j << std::endl;
    j++;
  }
  //do while
  int k = 100;
  do {
    std::cout << "3.El: " << j << std::endl;
    k-=10;
  } while (k<10);
  return 0;
}
