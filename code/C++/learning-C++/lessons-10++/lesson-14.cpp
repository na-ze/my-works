#include <iostream>
#include <iterator>
#include <ostream>
#include <string>
using namespace std;

struct Point{
  int x,y;
};

struct Tree{
  string name;
  int age;
  bool is_alive;
  float height;
  Point place;

  void get_info() {
    cout << "Name: " << name << ". Age: " << age << endl;
  }
};

int main () {
  
  Tree dub;
  dub.name = "Дуб";
  dub.age = 24;
  dub.place.x = 1;
  dub.place.y = 10;

  Tree yelka;
  yelka.name = "Ёлка";
  yelka.age = 5;
  yelka.place.x = 50;
  yelka.place.y = 10;

  //cout << dub.name << " - " << yelka.name << endl;
  //cout << dub.age << " - " << yelka.age << endl;

  dub.get_info();
  yelka.get_info();

  return 0;
}
