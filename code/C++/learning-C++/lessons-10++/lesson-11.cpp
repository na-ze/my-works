#include <iostream>
#include <string>
using namespace std;

void print(string word);
void print(int word);
void add(int a,int b);
void add(int a,int b,int y);

int main () {
  print("some");
  add(5,6);
  add(5,6,5);
  return 0;
}

void print(string word){
  cout << word << endl;
}
void print(int word){
  cout << word << endl;
}
void add(int a,int b){
  int res=a+b;
  print(res);
}
void add(int a,int b,int y){
  int res=a+b+y;
  print(res);
}
