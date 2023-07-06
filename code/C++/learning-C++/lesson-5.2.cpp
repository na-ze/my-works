#include <time.h>
#include <iostream>
using namespace std;

int main () {
  srand(time(NULL));

  int result = 1 + rand() % 20;  
  cout << result << endl;



  return 0;
}
