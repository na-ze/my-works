#include <iostream>
#include <string>
using namespace std;

void minimal (int *arr, int len);

int main () {
  //Практический пример
  int arr[] = {5,7,3,-2,5};
  minimal(arr, 5);
  return 0;
}
void minimal (int *arr, int len){
  int min = *arr;
  for(int i=0;i<len;i++){
    if(min > *(arr + i))
      min = *(arr + i);
  }
  cout << "Minimal: " << min << endl;
}
