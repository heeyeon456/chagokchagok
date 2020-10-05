// 포토캐논
#include <string.h>
#include <iostream>

class Photon_Cannon {
  int hp, shield;
  int coord_x, coord_y;
  int damage;

 public:
  Photon_Cannon(int x, int y);
  //Photon_Cannon(const Photon_Cannon& pc); // 디폴트로 복사 생성자 제공

  void show_status();
};
// 복사 생성자
// T(const T& a);
// 다른 T의 객체 a를 생수 레퍼런스로 받는다. 
// a가 const 니깐 내부에서 a값을 변경할 수는 없고, 새롭게 초기화된 인스턴스 변수들에게 복사만 할 수 있다. 
/*Photon_Cannon::Photon_Cannon(const Photon_Cannon& pc) {
  std::cout << "복사 생성자 호출 !" << std::endl;
  hp = pc.hp;
  shield = pc.shield;
  coord_x = pc.coord_x;
  coord_y = pc.coord_y;
  damage = pc.damage;
}*/
Photon_Cannon::Photon_Cannon(int x, int y) {
  std::cout << "생성자 호출 !" << std::endl;
  hp = shield = 100;
  coord_x = x;
  coord_y = y;
  damage = 20;
}
void Photon_Cannon::show_status() {
  std::cout << "Photon Cannon " << std::endl;
  std::cout << " Location : ( " << coord_x << " , " << coord_y << " ) "
            << std::endl;
  std::cout << " HP : " << hp << std::endl;
}
int main() {
  Photon_Cannon pc1(3, 3);
  Photon_Cannon pc2(pc1); // 복사 생성자 호출 (p1의 값이 p2로 복사됨)
  Photon_Cannon pc3 = pc2; // 복사 생성자 호출 (복사 생성자는 생성시에만 호출됨)
  // p3 = p2; // 생성단계가 아니므로, 복사생성자 호출이 아닌 단순 대입

  pc1.show_status();
  pc2.show_status();
}