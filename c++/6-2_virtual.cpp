#include <iostream>

class Base {

 public:
  Base() { std::cout << "기반 클래스" << std::endl; }

  // virtial
  // 클래스에 의해서 메소드가 호출됐을 떄 정말 해당 클래스의 객체가 맞는지 한번 더 확인
  // 컴파일 시에 어떤 함수가 실행될 지 정해지지 않고 런타임시에 정해지는 일 : 동적 바인팅 (Dynamic Binding)
  // virtual function
  virtual void what() { std::cout << "기반 클래스의 what()" << std::endl; }
  virtual ~Base() { std::cout << "Base의 소멸자 호출" << std::endl;}
};

class Derived : public Base {

 public:
  Derived() : Base() { std::cout << "파생 클래스" << std::endl; }

    // override 키워드를 통해서 override 하는 사실을 명시적으로 나타낼 수 있음
  void what() override { std::cout << "파생 클래스의 what()" << std::endl; }
  ~Derived() { std::cout << "Derived의 소멸자 호출" << std::endl; }
};

int main() {
  Base p;
  Derived c;

  Base* p_c = &c;
  Base* p_p = &p;
  

  std::cout << " == 실제 객체는 Base == " << std::endl;
  p_p->what();


  std::cout << " == 실제 객체는 Derived == " << std::endl;
  p_c->what(); // Base 클래스로 형변환을 했음에도, Derived class의 what을 호출한다.  -> virtual 의 역할

  Base *b = new Base();
  Base *e = new Derived();
  Derived *d = new Derived();

  std::cout << "b" << std::endl;
  delete b;
  std::cout << "d" << std::endl;
  delete d;
  std::cout << "e" << std::endl;
  delete e;

  return 0;
}