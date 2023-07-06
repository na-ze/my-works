#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

int main () {
  srand(time(NULL));
  int rand_num = 1+rand() % 15;
  bool stop = false;
  int user_input;

  cout << "Это игра, тебе нужно угадать число от 1, до 15, подсказок не будет, удачи)" << endl;

  do {
    cout << "Enter number: ";
    cin >> user_input;

    if(user_input != rand_num)
      cout << "Вы не угадали" << endl;

    else
      stop = true;
  } while (!stop);

  cout << "Вы угадали" << endl;
  return 0;
}
