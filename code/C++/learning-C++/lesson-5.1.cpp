#include <iostream>

using namespace std;

int main () {
  float num1, num2, res;
  cout << "Enter num1: ";
 cin >> num1;

  char math;
  cout << "Enter math symbol: ";
  cin >> math;

  cout << "Enter num2: ";
  cin >> num2;

  switch (math) {
    case '+': res = num1 + num2; break;
    case '-': res = num1 - num2; break;
    case '*': res = num1 * num2; break;
    case '/': res = num1 / num2; break;
    default:
      res = 0;
      cout << "Error, please try again" << endl;
      break;
  }
  cout << "Result: " << res << endl;
  return 0;
}

 // if(math=='+')
 //   res = num1 + num2;
 // else if (math=='-')
 //   res = num1 - num2;
 // else if (math=='*')
 //   res = num1 * num2;
 // else if (math=='/')
 //   res = num1 / num2;
