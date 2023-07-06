#include <iostream>
using namespace std;

int main () {
  float numbers[5];
  for(int i=0;i<5;i++){
    cout << "Enter number" << i << ": " ;
    cin >> numbers[i];
  }
  
  float summa = 0;
  float min = numbers[0];
  for(int i=0;i<5;i++){
    summa+=numbers[i];
    if(numbers[i]<min)
      min = numbers[i];
  }
  cout << "Summa: " << summa << endl;
  cout << "Min: " << min << endl;

  for(int i=0;i<5;i++)
    cout << "Element: " << numbers[i] << endl;







  return 0;
}
