#include <iostream>
#include <string>

class Base {
  std::string s;

 protected:
  std::string parent_string;

 public:
  Base() : s("기반"), parent_string("원래") {  std::cout << "기반 클래스" <<  std::endl; }

  void what() {  std::cout << s <<  std::endl; }
  void print_string() { std::cout << parent_string << std::endl; }
};

// 어떤 형식으로 상속받느냐에 따라서 클래스의 멤버들이 실제로 어떻게 작동하는지 영향을 준다.
// - public : 기반 클래스의 접근 지시자들에 영향없이 그대로 작동 (public -> public, private -> private)
// - protected : (public -> protected, private-> private)
// - private: 모든 접근 지시자들이 private 이 된다. 
// Derived 가 Base를 public 형식으로 상속받겠다
class Derived : public Base {
  std::string s;
  std::string child_string;

 public:
 // Devived 객체 생성 전에 Base이 생성자를 먼저 호출!
  Derived() : s("파생"), child_string("파생"), Base() {
     std::cout << "파생 클래스" <<  std::endl;
래
    // Base 에서 what() 을 물려 받았으므로
    // Derived 에서 당연히 호출 가능하다
    what();

    // private 변수인 Base의 parent string에 접근할 수 있나? -> protected 로 바꾸면됨
    // protected: 상속받는 클래스에서는 접근 가능하고 그 외의 기타 정보는 접근 불가능
    parent_string = "바꾸기";
  }
  // 이름이 같아도 다른 클래스에 정의되어 있기 때문에 다른 함수로 취급됨
  // overriding
  // Derived 의 what 함수가 Base 의 what 함수를 오버라이딩!
  void what() { std::cout << s << std::endl; } 
  void print_string() { std::cout << child_string << parent_string << std::endl; }
};
int main() {
   std::cout << " === 기반 클래스 생성 ===" <<  std::endl;
  Base p;
  p.print_string();

   std::cout << " === 파생 클래스 생성 ===" <<  std::endl;
  Derived c;
  c.print_string();

  return 0;
}