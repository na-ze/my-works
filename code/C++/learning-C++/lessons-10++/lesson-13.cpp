#include <ios>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
  
  /*ofstream file("test.txt", ios_base::out);
  if(file.is_open()){
    file << "Hello World";
    file.close();
  }
  */

  ifstream file("test.txt");
  if(file.is_open()){
      //string temp;
      //file >> temp;  output only ONE WORD
  char temp[100];
  file.getline(temp, 100);
  cout << temp << endl;
  file.close();
  }








  return 0;
}
