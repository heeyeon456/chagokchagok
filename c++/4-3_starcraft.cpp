#include <string.h>
#include <iostream>

class Marine {
  int hp;                // 마린 체력
  int coord_x, coord_y;  // 마린 위치
  int damage;            // 공격력
  bool is_dead;
  char* name;

 public:
  Marine();              // 기본 생성자
  Marine(int x, int y, const char* name);  // x, y 좌표에 마린 생성

  int attack();                       // 데미지를 리턴한다.
  void be_attacked(int damage_earn);  // 입는 데미지
  void move(int x, int y);            // 새로운 위치

  void show_status();  // 상태를 보여준다.

  ~Marine(); // 소멸자
};
Marine::Marine() {
  hp = 50;
  coord_x = coord_y = 0;
  damage = 5;
  is_dead = false;
}
Marine::Marine(int x, int y, const char* marine_name) {
  name = new char[strlen(marine_name)+1];
  strcpy(name, marine_name);
  coord_x = x;
  coord_y = y;
  hp = 50;
  damage = 5;
  is_dead = false;
}
void Marine::move(int x, int y) {
  coord_x = x;
  coord_y = y;
}
int Marine::attack() { return damage; }
void Marine::be_attacked(int damage_earn) {
  hp -= damage_earn;
  if (hp <= 0) is_dead = true;
}
void Marine::show_status() {
  std::cout << " *** Marine *** " << std::endl;
  std::cout << " Location : ( " << coord_x << " , " << coord_y << " ) "
            << std::endl;
  std::cout << " HP : " << hp << std::endl;
}
// 소멸자 (Destructor)
// 객체가 소멸될 때, 자동으로 호출되는 소멸자
// 생성자에서 이름에 대한 char형 배열을 동적으로 할당해놨으므로 이는 따로 해제해줘야 한다.
Marine::~Marine() {
    std::cout << name << " 의 소멸자 호출 !" << std::endl;
    if (name != NULL) { delete[] name; }
 }

int main() { 
    Marine* marines[100]; // 여러 마린들이 나올수 있으니깐 Marine class의 instance 의 집합으로 표현

    // new와 malloc 은 동적으로 메모리를 할당한다는 점에서 의미가 있지만,
    // new의 경우 객체를 동적으로 생성하면서, 자동으로 생성자도 호출해준다.
    marines[0] = new Marine(2, 3, "Marine 2"); 
    marines[1] = new Marine(3, 5, "Marine 1");
    // 이렇게 char 포인터를 heap 안에 할당

    // marine 들의 포인터를 가리키는 배열이기 때문에 메소드 호출 시 -> 를 사용해야 한다. 
    marines[0]->show_status();
    marines[1]->show_status();

    std::cout << std::endl << "마린 1 이 마린 2 를 공격! " << std::endl;

    marines[0]->be_attacked(marines[1]->attack());

    marines[0]->show_status();
    marines[1]->show_status();

    // 동적으로 할당된 메모리는 언제나 해제해줘야 한다. 
    delete marines[0];
    delete marines[1];
    // marine instance 에 대한 메모리는 해제되지만 내부에 정의된 name 에 대한 메모리 할당은 해제 안된다 -> 메모리 누수 발생!

}