#include <iostream>
#include <string>
using namespace std;

void print(string word);
int add(int a,int b);

int main () {
  //print("Hello");
  //string words = "World";
  //print(words);
  //print("!!!");
  print("Sum: "); // std::cout << "Sum: " << std::endl;
 
  int res1 = add(5,7);
  int res2 = add(51,7);
  if(res1 > res2){
    print("res1: ");
    cout << res1 << endl;
  }
  else{
    print("res2: ");
    cout << res2 << endl;
  }
  return 0;
}

void print(string word) {
  cout << word;
}
int add(int a,int b) {
  return a+b;
}

