#include <iostream>

class Marine {
  // static 멤버 변수: 마치 전역 변수 같이 기능하지만 클래스 하나에 종속된ㄴ 변수
  static int total_marine_num;
  const static int i = 0;

  int hp;                // 마린 체력
  int coord_x, coord_y;  // 마린 위치
  bool is_dead;

  const int default_demage; //기본 공격력

 public:
  Marine();              // 기본 생성자
  Marine(int x, int y);  // x, y 좌표에 마린 생수
  Marine(int x, int y, int default_demage); // 새로운 생성자

  // const 함수
// (기존 함수의 정의) const;
  int attack() const   ;                   // 데미지를 리턴한다.
  Marine& be_attacked(int damage_earn);  // 입는 데미지
  void move(int x, int y);            // 새로운 위치

  void show_status();  // 상태를 보여준다.
  // static 함수
  // 특정 객체에 종속되는 것이 아니라 클래서 전체에 딱 한개만 존재하는 함수!
  static void show_total_marine();
  ~Marine() { total_marine_num--; }
};

//static int member 변수 초기화
int Marine::total_marine_num = 0;
void Marine::show_total_marine() {
  //std::count << default_demage // 이 경우 static 변수인 show_total_marine은 어떤 객체의 default demage인지 모름
  // static 함수는 객체가 아닌 클래스에 종속되기 때문
  std::cout << "전체 마린 수: " << total_marine_num << std::endl;
}

// 기존의 생성자와 다르게 정의됨
// 초기화 리스트 (initializer list)
//(생성자 이름) : var1(arg1), var2(arg2) {}
Marine::Marine() 
    : hp(50), coord_x(0), coord_y(0), default_demage(5), is_dead(false) {
      total_marine_num++;
    }

// 생성과 초기에를 동시에 (복사 생성자)
Marine::Marine(int x, int y)
    : coord_x(x), coord_y(y), hp(50), default_demage(5), is_dead(false) {
      total_marine_num++;
    }
// 그냥 생성자를 사용하면, 생성을 먼저하고 그다음에 대입 (디폴트 생성자)

Marine::Marine(int x, int y, int default_demage)
    : coord_x(x), 
      coord_y(y),
      hp(50),
      default_demage(default_demage),
      is_dead(false) {
        total_marine_num++;
      }

void Marine::move(int x, int y) {
  coord_x = x;
  coord_y = y;
}
// const 함수: 변수의 value를 바꾸지 않고 읽기만 하는, 마치 상수 같은 멤버함수를 '상수 함수' f로써 선언할 수 있따.
// 다른 변수의 값을 바꾸지 않는 함수(객체들의 읽기만 수행됨!)
int Marine::attack() const { return default_demage; }
Marine& Marine::be_attacked(int damage_earn) {
  hp -= damage_earn; // this->hp -= damage_earn;
  if (hp <= 0) is_dead = true; // if (this->hp <= 0) this->is_dead = true;
  // this 는 객체 자신을 가리키는 포인터 역할(멤버 함수를 호출하는 객체 자신을 가리킴)
  //Marine&을 리턴한다는 것? 레퍼런스(별명-alias) 를 리턴한다. 4_4_ref_func.cpp
  return *this;
}
void Marine::show_status() {
  std::cout << " *** Marine *** " << std::endl;
  std::cout << " Location : ( " << coord_x << " , " << coord_y << " ) "
            << std::endl;
  std::cout << " HP : " << hp << std::endl;
  std::cout << "현재 총 마린 수: " << total_marine_num << std::endl;
}
void create_marine() {
  Marine marine3(10, 10, 4);
  marine3.show_status();
}
int main() {
  Marine marine1(2, 3, 10);
  // static 함수는 어떤 객체에 종속되는 것이 아니라 클래스에 종속되는것!
  // (객체).(멤버함수) 로 호출하지 않고, (클래스)::(static 함수) 로 호출된다. 
  Marine::show_total_marine();

  Marine marine2(3, 5, 10);
  Marine::show_total_marine();

  marine1.show_status();
  marine2.show_status();
  create_marine();

  std::cout << std::endl << "마린 1 이 마린 2 를 두번 공격! " << std::endl;
  // 앞의 함수 실행으로 Marine 객체에 대한 reference 가 return 되고 이에 대해 be_attacked 함수를 바로 실행할 수 있다. 
  marine2.be_attacked(marine1.attack()).be_attacked(marine1.attack()); 

  marine1.show_status();
  marine2.show_status();


}