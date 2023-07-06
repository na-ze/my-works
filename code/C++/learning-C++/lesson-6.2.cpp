#include <iostream>

using namespace std;

int main () {
  // Операторы в циклах
  for(int i = 1; i<15; i++) {
    if (i == 10)
      break;
    if (i % 2 == 0)
      continue;

    cout << "EL: " << i << endl;
  }
  return 0;
}
