#include <iostream>
#include <string>
using namespace std;

int main () {
  //In C!
  char word[] ="Hi!";//{'H','i','!'}
  for(int i=0;i<3;i++)
    cout << word[i];
    //getline(cin,word)
  //In C++
  string words = "Hello World!";
  words[0] = 'W';
  cout << "\n" << words << endl;

  cin >> words;
  cout << "New:" << words << endl;









  return 0;
}
